from article.models import Article


def sidebar_processor(request):
    return {
        'sidebar_comments': Article.objects.filter(type=Article.COMMENT).order_by('-weight')[:10]
        }