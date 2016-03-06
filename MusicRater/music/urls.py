from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from music.models import Music
from music.views import  *


urlpatterns = patterns('',
         url(r'^$', 'music.views.musicRating',name ="music_rating"),
		 # url(r'?(<p>)','music.views.musicType' , name = 'song_types'),
		 url(r'(?P<songs>\w+)$' ,'music.views.musicType')
		 )



						