from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from articles.models import News
from articles.views import  *


urlpatterns = patterns('',
                        url(r'^$', 'articles.views.articles',name ="latest_articles"),
						url(r'(?P<article_id>\d+)$' ,'articles.views.listOfArticles'),
						
)



						