import os
from frontdoor.models.articles import Article
from frontdoor.models.gallery_items import GalleryItem
from django.conf import settings

FONTSET = ['Mukta', 'Oswald', 'Raleway', 'Kalam']


def fetch_articles(titles=[]):
    selection = Article.objects.filter(title__in=titles)
    return selection


def populate_gallery(path):
    target_path = os.path.join(settings.MEDIA_ROOT, path)
    onlyfiles = [f for f in os.listdir(target_path) if os.path.isfile(os.path.join(target_path, f))]
    for f in onlyfiles:
        full_name = f'{path}{f}'
        tracked = GalleryItem.objects.filter(image_reference=full_name)
        if len(tracked) == 0:
            gi = GalleryItem(image_reference=full_name)
            gi.image_short = f
            gi.image_path = path
            gi.generate_crop()
            gi.save()
        else:
            gi = GalleryItem.objects.filter(image_reference=full_name).first()
            gi.generate_crop()
