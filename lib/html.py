import re
import base64
import uuid
from io import BytesIO
from urllib.parse import urlsplit

from PIL import Image

import lxml.html
import lxml.html.clean

from django.core.files.base import ContentFile

from leaza import settings


class MyCleaner(lxml.html.clean.Cleaner):
    def allow_embedded_url(self, el, url):
        if (self.whitelist_tags is not None
            and el.tag not in self.whitelist_tags):
            return False
        scheme, netloc, path, query, fragment = urlsplit(url)
        netloc = netloc.lower().split(':', 1)[0]
        if scheme not in ('http', 'https', ''):
            return False
        if netloc in self.host_whitelist:
            return True
        return False


def sanitize(data):
    cleaner = MyCleaner(add_nofollow=True, host_whitelist=['www.youtube.com'], whitelist_tags=['iframe'])

    return cleaner.clean_html('<div>%s</div>' % data)


def extract_images(article, data, ImageModel):
    html = lxml.html.fromstring(data)

    found = False
    for img in html.findall(".//img") + ([html] if html.tag == 'img' else []):
        src = img.attrib['src']
        if not src.startswith('data:'):
            # nothing to do
            continue

        # extract the image data
        data_re = re.compile(r'data:(?P<mime_type>[^"]*);(?P<encoding>[^"]*),(?P<data>[^"]*)')
        m = data_re.search(src)
        dr = m.groupdict()
        mime_type = dr['mime_type']
        image_data = dr['data']
        if mime_type.find(";"):
            mime_type = mime_type.split(";")[0]
        try:
            image_data = base64.b64decode(image_data)
        except:
            image_data = base64.urlsafe_b64decode(image_data)
        try:
            image_type = mime_type.split("/")[1]
        except IndexError:
            # No image type specified -- will convert to jpg below if it's valid image data
            image_type = ""
        image = BytesIO(image_data)
        im = Image.open(image)

        # genarate filename and normalize image format
        if image_type == "jpg" or image_type == "jpeg":
            file_ending = "jpeg"
        elif image_type == "png":
            file_ending = 'png'
        elif image_type == "gif":
            file_ending = "gif"
        else:
            # any not "web-safe" image format we try to convert to jpg
            new_image = BytesIO()
            file_ending = "jpeg"
            im.save(new_image, "JPEG")
            new_image.seek(0)
            image = new_image

        if im.size[0] > settings.MAX_IMAGE_WIDTH or im.size[1] > settings.MAX_IMAGE_HEIGHT:
            im.thumbnail((settings.MAX_IMAGE_WIDTH, settings.MAX_IMAGE_HEIGHT))
            new_image = BytesIO()
            im.save(new_image, file_ending)
            new_image.seek(0)
            image = new_image

        width = getattr(img.attrib, 'width', None)
        height = getattr(img.attrib, 'height', None)
        if not width or not height:
            width, height = im.size

        filename = u"%d-%s.%s" % (article.pk, uuid.uuid4(), file_ending)

        image_object = ImageModel.objects.create(
            article=article
        )
        image_object.image.save(filename, ContentFile(image.getvalue()))
        img.attrib['src'] = image_object.image.url
        img.attrib['width'], img.attrib['height'] = [str(x) for x in im.size]
        found = True

    if found:
        return lxml.html.tostring(html), found
    else:
        return data, found