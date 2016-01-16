from django.core.mail import send_mail
from django.dispatch import receiver

from article.signals import article_was_created
from .settings import SITE_URL

@receiver(article_was_created)
def my_callback(sender, **kwargs):
    send_mail('Article was created', '%s %s' % (kwargs['article'].title, SITE_URL + kwargs['article'].get_absolute_url()),
        None,
        ['admitrievsky@gmail.com'], fail_silently=True)
