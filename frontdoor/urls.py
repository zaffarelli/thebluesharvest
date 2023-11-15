from django.urls import re_path
from frontdoor.views import index, demo, presentation, concerts, medias, home, compositions, music, contacts, videos


urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^demo$', demo, name='demo'),
    re_path(r'^presentation$', presentation, name='presentation'),
    re_path(r'^concerts$', concerts, name='concerts'),
    re_path(r'^medias$', medias, name='medias'),
    re_path(r'^home$', home, name='home'),
    re_path(r'^compositions$', compositions, name='compositions'),
    re_path(r'^videos$', videos, name='videos'),
    re_path(r'^music$', music, name='music'),
    re_path(r'^contacts$', contacts, name='contacts'),
]