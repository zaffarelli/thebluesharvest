from django.urls import re_path
from frontdoor.views import index, demo, presentation, concerts, medias, home


urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^demo$', demo, name='demo'),
    re_path(r'^presentation$', presentation, name='presentation'),
    re_path(r'^concerts$', concerts, name='concerts'),
    re_path(r'^medias$', medias, name='medias'),
    re_path(r'^home$', home, name='home'),
]