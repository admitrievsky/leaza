import json

from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect, Http404
from django.forms import HiddenInput
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _

from .models import Article, CommentTree
from .forms import AddForm, EditForm, CommentAddForm

from .signals import article_was_created

def full_view(request, slug):
    article = get_object_or_404(Article, slug=slug)

    comment_form = CommentAddForm(request.POST if request.method == 'POST' else None)
    if request.user.pk:
        comment_form.fields['author_name'].widget = HiddenInput()
        comment_form.fields['author_name'].required = False

    if comment_form.is_valid():
        cd = comment_form.cleaned_data
        comment = Article.objects.create(
            title='Comment for %d' % (article.pk),
            content=cd['content'],
            type=Article.COMMENT,
            author=request.user if request.user.pk else None,
            author_name=cd['author_name'] if not request.user.pk else None
        )
        if cd['parent']:
            parent = Article.objects.get(pk=int(cd['parent']))
            assert parent.type == Article.COMMENT
            assert CommentTree.objects.get(content=parent).root == article
            CommentTree.objects.create(
                root=article,
                parent=parent,
                content=comment)
        else:
            CommentTree.objects.create(
                root=article,
                parent=article,
                content=comment)

        article_was_created.send('account:full_view', article=comment)

        return redirect(comment)

    return render(request, 'article/full.html', {
        'article': article,
        'add_edit_link': article.can_edit(request.user),
        'comment_form': comment_form
    })


def add(request):
    form = AddForm(request.POST if request.method == 'POST' else None)

    if request.user.pk:
        form.fields['author_name'].widget = HiddenInput()
        form.fields['author_name'].required = False

    if form.is_valid():
        cd = form.cleaned_data
        article = Article.objects.create(
            title=cd['title'],
            content=cd['content'],
            type=Article.ARTICLE,
            author=request.user if request.user.pk else None,
            author_name=cd['author_name'] if not request.user.pk else None
        )
        article_was_created.send('account:full_view', article=article)
        return redirect(article)


    return render(request, 'article/edit.html', {
        'article': None,
        'form': form,
        'action_button': _('Post!'),
        'action': _('Post')
    })


def edit(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if not article.can_edit(request.user):
        raise Http404

    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            article.title = cd['title']
            article.content = cd['content']
            article.save()
            article_was_created.send('account:full_view', article=article)
            return redirect(article)
    else:
        form = EditForm(initial={
            'title': article.title,
            'content': article.get_content()
        })


    return render(request, 'article/edit.html', {
        'article': None,
        'form': form,
        'action': _('Edit'),
        'action_button': _('Edit')
    })


def vote(request):
    if not request.user.is_authenticated():
        return HttpResponseForbidden()
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        a = Article.objects.get(pk=data['id'])
        a.vote(request.user, data['mark'])
        return JsonResponse({'now': a.rating})
    else:
        raise Http404()