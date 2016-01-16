from django.shortcuts import render, get_object_or_404, Http404, redirect
from .models import Account
from article.models import Article
from lib.listing import listing
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
import io
import PIL.Image
from django.core.files.base import ContentFile
from django.contrib.auth import logout as do_logout, login as do_login
from django.contrib.auth.forms import AuthenticationForm
from django.dispatch import receiver
from django.contrib.auth import authenticate

from registration.backends.simple.views import RegistrationView as RegistrationViewOriginal
from registration import signals as registration_signals
from registration import signals

from .forms import AccountForm, RegistrationForm


def display(request, slug=None):
    if slug:
        account = get_object_or_404(Account, slug=slug)
    else:
        if request.user.is_authenticated():
            account = request.user
        else:
            raise Http404()

    return render(request, 'account/display.html', {
        'account': account,
        'can_edit': account.can_edit(request.user),
        'articles': listing(
            request,
            Article.objects.filter(type=Article.ARTICLE, author=account).order_by('-rating', 'weight')
        )
    })


@login_required
def edit(request, slug):
    account = get_object_or_404(Account, slug=slug)

    if not account.can_edit(request.user):
        raise Http404()

    recreate_form = True

    if request.method == 'POST':
        recreate_form = False
        form = AccountForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            if not cd['last_name'] and not cd['first_name']:
                cd['last_name'] = account.user.username

            account.first_name = cd['first_name']
            account.last_name = cd['last_name']
            account.save()

            if cd['image']:
                image_io = io.BytesIO(cd['image'].read())
                image_pil = PIL.Image.open(image_io)
                image_pil.thumbnail((256, 256))
                new_image = io.BytesIO()
                image_pil.save(new_image, 'jpeg')
                new_image.seek(0)

                account.image.save(slugify(account.username) + '.' + '.jpg',
                   ContentFile(new_image.read()))

            recreate_form = True

    if recreate_form:
        form = AccountForm(initial={
            'first_name': account.first_name,
            'last_name': account.last_name if account.last_name or account.first_name else account.username,
        })

    return render(request, 'account/edit.html', {
        'account': account,
        'form': form,
        'is_owner': request.user.username == account.username
    })


@login_required
def logout(request):
    do_logout(request)
    return redirect('home')


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Okay, security check complete. Log the user in.
            do_login(request, form.get_user())

            return redirect('account:display-current')
    else:
        form = AuthenticationForm(request)

    return render(request, 'account/login.html' if not request.GET.get('xhr') else 'account/_login.html', {
        'form': form
    })



class RegistrationView(RegistrationViewOriginal):
    template_name = 'account/registration.html'
    form_class = RegistrationForm

    def register(self, request, **cleaned_data):
        username, email, password = cleaned_data['username'], cleaned_data['email'], cleaned_data['password1']
        Account.objects.create_user(username, email, password, last_name=username)

        new_user = authenticate(username=username, password=password)
        do_login(request, new_user)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)
        return new_user

    def get_success_url(self, request, user):
        return user.get_edit_url()