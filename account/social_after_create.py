import json
import urllib.request
import io
import PIL.Image

from django.utils.text import slugify
from django.core.files.base import ContentFile

from account.models import Account


def social_after_create(backend, user, response, *args, **kwargs):
    user.social_raw = json.dumps({
        'backend': backend.name,
        'data': response
    })

    try:
        url = None
        print(backend.name)
        if backend.name == 'facebook':
            url = "http://graph.facebook.com/%s/picture?type=large" % response["id"]
        elif backend.name == 'google-oauth2':
            url = response["image"]['url']
        elif backend.name == 'odnoklassniki-oauth2':
            url = response['pic_2']
        elif backend.name == 'vk-oauth2':
            url = response['photo']
        elif backend.name == 'mailru-oauth2':
            url = response['pic_big']

        if url:
            with urllib.request.urlopen(url) as image_response:
                image_io = io.BytesIO(image_response.read())
                image_pil = PIL.Image.open(image_io)
                image_io.seek(0)
                user.image.save(slugify(user.username + " social") + '.' + image_pil.format.lower(),
                                   ContentFile(image_io.read()))

    except urllib.request.HTTPError:
        pass

    user.save()
