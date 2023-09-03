from django.db import models
from django.contrib import admin
from datetime import datetime
from PIL import Image
from django.conf import settings
import math


class GalleryItem(models.Model):
    image_reference = models.CharField(max_length=256,unique=True)
    image_short = models.CharField(default='', max_length=256)
    image_path = models.CharField(default='', max_length=256)
    ox = models.PositiveIntegerField(default=0, blank=True)
    oy = models.PositiveIntegerField(default=0, blank=True)
    ow = models.PositiveIntegerField(default=15, blank=True)
    oh = models.PositiveIntegerField(default=60, blank=True)

    def _str_(self):
        return f'{self.pk}_{self.image_reference}'

    def generate_crop(self):
        with Image.open(settings.MEDIA_ROOT+self.image_path+self.image_short) as img:
            img.load()
            w, h = img.size
            ow = self.ow #math.floor(w * (self.ow/100))
            oh = self.oh #math.floor(h * (self.oh/100))
            ox = self.ox #math.floor(w * (self.ox/100))
            oy = self.oy #math.floor(h * (self.oy/100))
            cropped_img = img.crop((ox, oy, ox+ow, oy+oh))
            cropped_img.resize((ow,oh),Image.Resampling.LANCZOS)
            n = f"{self.image_path}thumbnails/crop_{self.image_short}"
            print(n)
            cropped_img.save(settings.MEDIA_ROOT+n)


class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ['image_reference', 'ox', 'oy', 'ow','oh']
    search_fields = ['image_reference']
    list_editable = ['ox', 'oy', 'ow','oh']

