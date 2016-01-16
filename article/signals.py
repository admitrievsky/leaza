import django.dispatch

article_was_created = django.dispatch.Signal(providing_args=["article"])
