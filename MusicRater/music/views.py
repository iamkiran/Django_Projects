from django.shortcuts import render
from music.models import Music
import random

# Create your views here.
def musicRating(request):
	TOP3RATEDSONGS = 3 ;
	
	musicModel = Music.objects.all() 
	
	context = {'musicRecords': musicModel ,  
	   'title' : 'Music Rater' , 
	   'num_of_objects' : Music.objects.count() , 
	   'top3rated' : musicModel[0:3],
	   'song_list' : sorted(Music.SONG_CHOICES , key = lambda x:x[1]),


		}
	return render(request, 'base_music.html',context)

def musicType(request,songs):
	print request.GET.get('songType');
	
	musicModel = Music.objects.all(); 
	
	context = {'musicRecords': musicModel ,  
	   'title' : 'Music Rater' , 
	  
	   'selectedSongType' : request.GET.get('songType'),
		}
	return render(request, 'ajax_call.html',context)
