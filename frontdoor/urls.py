from django.urls import re_path
from frontdoor.views import index


urlpatterns = [
    re_path(r'^$', index, name='index')
]