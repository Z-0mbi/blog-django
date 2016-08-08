from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'blog.views.home', name='home'),
    url(r'^about/$', 'blog.views.about', name='about'),
    url(r'article/(?P<article_id>[0-9]+)/$', 'blog.views.article', name='article'),

]

