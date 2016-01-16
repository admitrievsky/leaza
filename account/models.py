from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

from django.core.urlresolvers import reverse

from lib.slugify import get_slug


class AccountManager(UserManager):
    pass


class Account(AbstractUser):
    objects = AccountManager()

    social_raw = models.TextField(null=True, blank=True)

    image = models.ImageField(upload_to='user_images', null=True, default='logo.png')

    slug = models.CharField(max_length=400, db_index=True)

    articles_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)

    article_rating = models.IntegerField(default=0)
    comment_rating = models.IntegerField(default=0)

    def can_edit(self, user):
        return user.pk == self.pk or user.is_staff

    def get_rating(self):
        return self.article_rating + self.comment_rating

    def get_absolute_url(self):
        return reverse('account:display', args=[self.slug])

    def get_edit_url(self):
        return reverse('account:edit', args=[self.slug])

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.id:
            self.slug = get_slug(Account, self.username)
        return super(Account, self).save(force_insert, force_update, using, update_fields)

    def __str__(self):
        fn = self.get_full_name()
        return fn if fn else self.username


Account._meta.get_field('username').max_length = 500
Account._meta.get_field('first_name').max_length = 500
Account._meta.get_field('last_name').max_length = 500
Account._meta.get_field('email').max_length = 500
