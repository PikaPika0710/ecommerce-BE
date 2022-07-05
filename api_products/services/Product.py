from io import BytesIO

from PIL import Image
from django.core.files import File


class ProductService:
    @classmethod
    def make_thumbnail(cls, image, size=(300, 300)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        thumbnail = File(thumb_io, name=image.name)
        return thumbnail
