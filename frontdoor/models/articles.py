from django.db import models
from django.contrib import admin
from django.urls import reverse
from datetime import datetime


class Article(models.Model):
    title = models.CharField(max_length=256)
    label = models.CharField(max_length=256, default='', blank=True)
    description = models.TextField(default='', max_length=4096, blank=True)
    pub_date = models.DateTimeField(default=datetime.now)
    author = models.CharField(default='', max_length=256, blank=True)
    display_title = models.BooleanField(default=False, blank=True)
    display_author = models.BooleanField(default=False, blank=True)

    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"pk": self.pk})

    def _str_(self):
        return f'{self.title}'


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'label', 'description', 'author', 'display_title', 'display_author']
    search_fields = ['title', 'description', 'author']
    list_editable = ['label', 'display_title', 'display_author', 'author']

