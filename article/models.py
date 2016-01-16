from collections import OrderedDict

from django.db import models, transaction
from django.core.urlresolvers import reverse

from lib import html
from lib.slugify import get_slug

from account.models import Account


class NotSignedInException(Exception):
    pass


class Article(models.Model):
    ARTICLE = 1
    COMMENT = 2

    author = models.ForeignKey(Account, null=True, blank=True)
    author_name = models.CharField(max_length=100, null=True, blank=True)
    type = models.IntegerField(choices=(
        (ARTICLE, 'Article'),
        (COMMENT, 'Comment')
    ))

    title = models.CharField(max_length=140)
    slug = models.CharField(max_length=400, db_index=True, editable=False)
    content = models.TextField()

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now_add=True, editable=False)   # Do not bother with initial data while creating
                                                                        # but update it manually before saving instance

    comment_count = models.IntegerField(default=0, editable=False)

    rating = models.IntegerField(default=0, editable=False)

    weight = models.FloatField(default=1000000, editable=False)

    def time_elapsed(self):
        return time_elapsed(self.created)

    def get_comment_count(self):
        return get_comment_count(self.comment_count)

    def get_author_display_name(self):
        return self.author.get_full_name() if self.author else self.author_name

    def get_content(self):
        return html.sanitize(self.content)

    def can_edit(self, user):
        return (self.author and self.author.username == user.username) or user.is_staff

    @transaction.atomic
    def vote(self, user, mark):
        assert abs(mark) < 2

        if not user.pk:
            raise NotSignedInException()

        author = self.author if self.author else None

        try:
            av = ArticleVote.objects.get(article=self, user=user)
            self.rating -= av.mark
            av.delete()

            if author:
                if self.type == Article.ARTICLE:
                    author.article_rating -= av.mark
                elif self.type == Article.COMMENT:
                    author.comment_rating -= av.mark
        except ArticleVote.DoesNotExist:
            pass
        ArticleVote.objects.create(article=self, user=user, mark=mark)

        self.rating += mark
        self.save()

        if author:
            if self.type == Article.ARTICLE:
                author.article_rating += mark
            elif self.type == Article.COMMENT:
                author.comment_rating += mark
            author.save()

    def get_comments(self):
        r = {'children': OrderedDict()}
        for c in CommentTree.objects.filter(root=self)\
                .select_related('content')\
                .order_by('position'):
            l = r
            for p in (int(x) for x in c.position.split('.')):
                l = l['children']
                l = l.setdefault(p, {'comment': None, 'children': OrderedDict()})
            l['comment'] = c.content
        return r['children']

    @transaction.atomic
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        assert (self.author is not None) ^ bool(self.author_name)

        if not self.id:
            self.slug = get_slug(Article, self.title)

            if self.author:
                if self.type == Article.ARTICLE:
                    self.author.articles_count += 1
                    self.author.save()
                elif self.type == Article.COMMENT:
                    self.author.comments_count += 1
                    self.author.save()

        r = super(Article, self).save(force_insert, force_update, using, update_fields)

        self.content, found = html.extract_images(self, self.content, ArticleImage)
        if found:
            return super(Article, self).save(force_update=True, using=using, update_fields=['content'])

    def get_absolute_url(self):
        if self.type == Article.ARTICLE:
            return reverse('article:full', args=[self.slug])
        else:
            return '%s#comment%d' % (
                reverse('article:full', args=[CommentTree.objects.get(content=self).root.slug]),
                self.pk
            )


class ArticleImage(models.Model):
    image = models.ImageField()
    article = models.ForeignKey(Article, related_name='images', editable=False)


class ArticleVote(models.Model):
    article = models.ForeignKey(Article, related_name='votes', editable=False, db_index=True)
    user = models.ForeignKey(Account, editable=False, db_index=True)
    when = models.DateTimeField(auto_now_add=True, editable=False)
    mark = models.IntegerField()


class CommentTree(models.Model):
    root = models.ForeignKey(Article, related_name='comments', editable=False, db_index=True)
    parent = models.ForeignKey(Article, related_name='comment_children', editable=False, db_index=True)
    content = models.OneToOneField(Article, related_name='comment_tree_entry', editable=False, db_index=True)
    position = models.TextField(max_length=200)

    @transaction.atomic
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        assert self.root
        assert self.content
        assert self.parent

        if not self.position:
            n = 0
            for c in self.parent.comment_children.all():
                n = max(n, int(c.position.split('.')[-1]))
            self.position = '%04d' % (n+1) if self.root == self.parent else \
                            '%s.%04d' % (self.parent.comment_tree_entry.position, n+1)

        super(CommentTree, self).save(force_insert, force_update, using, update_fields)

        self.root.comment_count += 1
        self.root.save()