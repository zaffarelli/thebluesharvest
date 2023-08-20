from django.db import models
from django.contrib import admin
from django.urls import reverse
from datetime import datetime


class Concert(models.Model):
    title = models.CharField(max_length=256)
    place = models.CharField(max_length=256, blank=True)
    contact = models.CharField(max_length=256, blank=True)
    image_ref = models.CharField(max_length=256, blank=True, null=True)
    pub_date = models.DateTimeField(default=datetime.now)
    perf_date = models.DateTimeField(default=datetime.now)
    is_private = models.BooleanField(default=False, blank=True)
    description = models.TextField(default='', max_length=4096, blank=True)
    notes = models.TextField(default='', max_length=2048, blank=True)

    def get_absolute_url(self):
        return reverse("concert-detail", kwargs={"pk": self.pk})

    def _str_(self):
        return f'{self.title} {self.perf_date} {self.place}'


class ConcertAdmin(admin.ModelAdmin):
    ordering = ['perf_date']
    list_display = ['title', 'place', 'description', 'notes',  'perf_date', 'is_private', 'contact', 'image_ref']
    search_fields = ['title', 'description', 'perf_date']
    list_editable = ['place', 'contact', 'perf_date', 'is_private', 'image_ref']
    list_filter = ["is_private"]

