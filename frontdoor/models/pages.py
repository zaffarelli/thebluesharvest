from django.db import models
from django.contrib import admin
from django.urls import reverse


class Page(models.Model):
    from frontdoor.models.articles import Article
    title = models.CharField(max_length=256)
    articles = models.ManyToManyField(Article)

    def get_absolute_url(self):
        return reverse("page-detail", kwargs={"pk": self.pk})

    def _str_(self):
        return f'{self.title}'

    def fix(self):
        title = self.title
        title = title.replace('é', 'e').replace('è', 'e').replace('ê', 'e').replace('ç', 'c').replace('ù', 'u').replace(
            'à', 'a').replace(' ', '_')
        title = title.upper()
        if title != self.title:
            self.title = title

    @property
    def articles_str(self):
        s = ""
        for a in self.articles.all():
            s += f'[{a.label}] '
        return s


class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'articles_str']
    search_fields = ['title']
