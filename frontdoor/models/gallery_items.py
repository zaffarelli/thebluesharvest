from django.db import models
from django.contrib import admin
from django.conf import settings
import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import PIL.ImageFont as ImageFont
import os

MAX_SIZE_PAYSAGE = (800, 600)
MAX_SIZE_PORTRAIT = (600, 800)


class GalleryItem(models.Model):
    image_reference = models.CharField(max_length=256, unique=True)
    image_short = models.CharField(default='', max_length=256)
    image_path = models.CharField(default='', max_length=256)
    ox = models.PositiveIntegerField(default=10, blank=True)
    oy = models.PositiveIntegerField(default=40, blank=True)
    ow = models.PositiveIntegerField(default=120, blank=True)
    oh = models.PositiveIntegerField(default=360, blank=True)
    not_found = models.BooleanField(default=False, blank=True)

    def _str_(self):
        return f'{self.pk}_{self.image_reference}'

    def generate_crop(self):
        img_name = settings.MEDIA_ROOT + self.image_path+'pictures/' + self.image_short
        print(f'Cropping... {img_name}.')

        with Image.open(img_name) as img:
            img.load()
            w, h = img.size
            ow = self.ow
            oh = self.oh
            ox = self.ox
            oy = self.oy
            cropped_img = img.crop((ox, oy, ox + ow, oy + oh))
            cropped_img.resize((ow, oh), Image.Resampling.LANCZOS)
            n = f"{self.image_path}thumbnails/{self.image_short}"
            print(f'Saving... {n}.')
            cropped_img.save(settings.MEDIA_ROOT + n)


    def watermark(self):
        img_name = settings.MEDIA_ROOT + self.image_path+'pictures/' + self.image_short
        print(f'Watermarking... {img_name}.')

        with Image.open(img_name) as img:
            img.load()
            w, h = img.size
            dr = ImageDraw.Draw(img)
            shadow = '#303030'
            text = 'silver'
            ft = ImageFont.truetype(settings.STATIC_ROOT + '/frontdoor/ttf/Lato-Black.ttf', 18)
            lft = ImageFont.truetype(settings.STATIC_ROOT + '/frontdoor/ttf/Lato-Black.ttf', 16)
            dr.rectangle((w - 265, h - 65, w, h - 10), fill='black')
            dr.text((w - 240, h - 60), "the Blues Harvest", font=ft, fill=shadow)
            dr.text((w - 238, h - 58), "the Blues Harvest", font=ft, fill=shadow)
            dr.text((w - 239, h - 59), "the Blues Harvest", font=ft, fill=text)
            dr.text((w - 240, h - 42), "2023", font=lft, fill=shadow)
            dr.text((w - 238, h - 40), "2023", font=lft, fill=shadow)
            dr.text((w - 239, h - 41), "2023", font=lft, fill=text)
            print(f'Saving... {img_name}.')
            img.save(self.image_path + "watermarked/" + self.image_short)


    def rescale(self):
        img_name = settings.MEDIA_ROOT + self.image_path+'pictures/' + self.image_short
        print(f'Rescaling... {img_name}.')
        with Image.open(img_name) as img:
            img.load()
            w, h = img.size
            img_resized = None
            if w >= h:  # Paysage
                if w > MAX_SIZE_PAYSAGE[0]:
                    img_resized = img.resize(MAX_SIZE_PAYSAGE)
            else:  # Portrait
                if h > MAX_SIZE_PORTRAIT[1]:
                    img_resized = img.resize(MAX_SIZE_PORTRAIT)
            if img_resized:
                img_resized.save(img_name)
                print(f'Resized: {img_name} ')
            else:
                print(f'Resized... nothing to do for {img_name} ')


    def prepare_all(self):
        self.rescale()
        self.generate_crop()
        self.watermark()


class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ['image_reference', 'ox', 'oy', 'ow', 'oh', 'not_found']
    search_fields = ['image_reference']
    list_filter = ['not_found']
    list_editable = ['ox', 'oy', 'ow', 'oh']
