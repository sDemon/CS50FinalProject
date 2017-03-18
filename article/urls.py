from django.conf.urls import url
from article.views import articles, article, addlike, addcomment

urlpatterns = [
    url(r'^articles/all/$', articles, name='articles'),
    url(r'^articles/get/(?P<article_id>\d+)/$', article, name='article'),
    url(r'^comments/article/(?P<comment_number>\d+)/$', article, name='article'),
    url(r'^articles/addlike/(?P<article_id>\d+)/$', addlike, name='addlike'),
    url(r'^articles/addcomment/(?P<article_id>\d+)/$', addcomment, name='addcomment'),
    url(r'^page/(\d+)/$', articles, name='articles'),
    url(r'^', articles, name='articles'),
]
