import os
import leaza.settings as settings
from django.test import TestCase
from .models import Article, CommentTree
from django.contrib.auth.models import User


class ArticleTestCase(TestCase):
    def setUp(self):
        pass

    def test_article_slugify(self):
        a = Article.objects.create(
            title='Фыв',
            content='asdфв',
            type=Article.ARTICLE,
            author_name='zxc'
        )
        a.save()
        self.assertEquals(a.slug, 'фыв')

        a = Article.objects.create(
            title='Фыв',
            content='asdфв',
            type=Article.ARTICLE,
            author_name='zxc'
        )
        a.save()
        self.assertRegexpMatches(a.slug, r'фыв-[\d]+')

        a = Article.objects.create(
            title='http://ya.ru/',
            content='asdфв',
            type=Article.ARTICLE,
            author_name='zxc'
        )

        a.save()
        self.assertEquals(a.slug, 'httpyaru')


    def test_image_extracting(self):
        with open(os.path.join(settings.BASE_DIR, 'article', 'test_data', 'gif_with_text')) as f:
            a = Article.objects.create(
                title='Фыв',
                content=f.read(),
                type=Article.ARTICLE,
                author_name='zxc'
            )
            self.assertEquals(a.images.count(), 1)

        with open(os.path.join(settings.BASE_DIR, 'article', 'test_data', 'huge_photo')) as f:
            a = Article.objects.create(
                title='Фыв',
                content=f.read(),
                type=Article.ARTICLE,
                author_name='zxc'
            )

            self.assertEquals(a.images.count(), 1)

    def test_youtube_video(self):
        a = Article.objects.create(
            title='Фыв',
            content='<iframe src="//www.youtube.com/embed/0f679wqZttE" width="640" height="360" frameborder="0" allowfullscreen=""></iframe>',
            type=Article.ARTICLE,
            author_name='zxc'
        )
        self.assertIn('0f679wqZttE', a.get_content())

    def test_not_youtube_video_other_iframes(self):
        a = Article.objects.create(
            title='Фыв',
            content='<iframe src="//www.yyoutube.com/embed/0f679wqZttE" width="640" height="360" frameborder="0" allowfullscreen=""></iframe>',
            type=Article.ARTICLE,
            author_name='zxc'
        )
        self.assertNotIn('0f679wqZttE', a.get_content())

    def test_votes(self):
        u = User.objects.create(username='test_account_votes')
        a = Article.objects.create(
            title='Фыв',
            content='asdфв',
            type=Article.ARTICLE,
            author_name='zxc'
        )
        a.save()

        a.vote(u, 1)
        self.assertEquals(a.rating, 1)
        a = Article.objects.get(pk=a.pk)
        self.assertEquals(a.rating, 1)

        a.vote(u, -1)
        self.assertEquals(a.rating, -1)

        a.vote(u, 0)
        self.assertEquals(a.rating, 0)

    def test_comments(self):
        a = Article.objects.create(
            title='Фыв',
            content='asdфв',
            type=Article.ARTICLE,
            author_name='zxc'
        )

        a0001 = Article.objects.create(title='Фыв', content='asdфв', type=Article.COMMENT, author_name='zxc')
        c = CommentTree.objects.create(root=a, parent=a, content=a0001)
        self.assertEquals(c.position, '0001')

        a0002 = Article.objects.create(title='Фыв', content='asdфв', type=Article.COMMENT, author_name='zxc')
        c = CommentTree.objects.create(root=a, parent=a, content=a0002)
        self.assertEquals(c.position, '0002')

        a0003 = Article.objects.create(title='Фыв', content='asdфв', type=Article.COMMENT, author_name='zxc')
        c = CommentTree.objects.create(root=a, parent=a, content=a0003)
        self.assertEquals(c.position, '0003')

        a0002_0001 = Article.objects.create(title='Фыв', content='asdфв', type=Article.COMMENT, author_name='zxc')
        c = CommentTree.objects.create(root=a, parent=a0002, content=a0002_0001)
        self.assertEquals(c.position, '0002.0001')

        a0003_0001 = Article.objects.create(title='Фыв', content='asdфв', type=Article.COMMENT, author_name='zxc')
        c = CommentTree.objects.create(root=a, parent=a0003, content=a0003_0001)
        self.assertEquals(c.position, '0003.0001')

        a0002_0002 = Article.objects.create(title='Фыв', content='asdфв', type=Article.COMMENT, author_name='zxc')
        c = CommentTree.objects.create(root=a, parent=a0002, content=a0002_0002)
        self.assertEquals(c.position, '0002.0002')

        a0003_0002 = Article.objects.create(title='Фыв', content='asdфв', type=Article.COMMENT, author_name='zxc')
        c = CommentTree.objects.create(root=a, parent=a0003, content=a0003_0002)
        self.assertEquals(c.position, '0003.0002')

        self.assertEquals(a.comment_count, 7)