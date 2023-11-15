import os
from frontdoor.models.articles import Article
from frontdoor.models.gallery_items import GalleryItem
from django.conf import settings
import shutil
import os

FONTSET = ['Mukta', 'Oswald', 'Raleway', 'Kalam', 'Anton', 'Kanit', 'Neuton', "Syne", 'Thasadith', 'Glory', 'Fresca','Farsan']


def fetch_articles(titles=[]):
    selection = Article.objects.filter(title__in=titles)
    return selection


def populate_gallery(path):
    """
    Populates the gallery from raw. Puts the relevant preview images
    """
    raw_path = os.path.join(settings.MEDIA_ROOT, path+"raw/")

    target_path = os.path.join(settings.MEDIA_ROOT, path+"pictures/")

    print("All the pathes: ",raw_path, target_path)

    # Remove the previous files in target
    onlyImagesFromTarget = [f for f in os.listdir(target_path) if os.path.isfile(os.path.join(target_path, f))]
    for f in onlyImagesFromTarget:
        os.remove(target_path+f)
        print(f"Removed: {target_path+f}")

    # Copy the images from raw to target
    onlyImagesFromRaw = [f for f in os.listdir(raw_path) if os.path.isfile(os.path.join(raw_path, f))]
    for f in onlyImagesFromRaw:
        shutil.copy(raw_path+f,target_path+f)
        print(f"Copied: {raw_path + f} --> {target_path + f}")

    onlyImagesFromTarget = [f for f in os.listdir(target_path) if os.path.isfile(os.path.join(target_path, f))]

    # Track each image
    for f in onlyImagesFromTarget:
        full_name = f'{path}{f}'
        print(full_name)
        tracked = GalleryItem.objects.filter(image_reference=full_name)
        if len(tracked) == 0:
            print("New GI entry")
            gi = GalleryItem(image_reference=full_name)
            gi.image_short = f
            gi.image_path = path
            # gi.save()
            # gi.reload()
            gi.prepare_all()
            gi.save()
        else:
            print("Updating GI entry")
            gi = GalleryItem.objects.filter(image_reference=full_name).first()
            gi.prepare_all()
            gi.not_found = False
            gi.save()



