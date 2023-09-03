from django.contrib import admin
from frontdoor.models.articles import Article, ArticleAdmin
from frontdoor.models.concerts import Concert, ConcertAdmin
from frontdoor.models.gallery_items import GalleryItem, GalleryItemAdmin

admin.site.register(Article, ArticleAdmin)
admin.site.register(Concert, ConcertAdmin)
admin.site.register(GalleryItem, GalleryItemAdmin)



