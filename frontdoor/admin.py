from django.contrib import admin
from frontdoor.models.articles import Article, ArticleAdmin
from frontdoor.models.concerts import Concert, ConcertAdmin

admin.site.register(Article, ArticleAdmin)
admin.site.register(Concert, ConcertAdmin)



