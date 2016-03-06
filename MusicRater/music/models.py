from django.db import models
from time import time


def artistIcon(instance , filename):

    return 'uploadedImg/artist/' + filename 
    	
def songsAlbum(instance , filename):
    return 'uploadedImg/album/'  + filename 
    	

class Music(models.Model):
    title = models.CharField("Song Title", max_length = 256)
    author_Detail = models.CharField("Artist" , max_length = 256)
    date = models.DateTimeField("Released Date")
    artist_img = models.ImageField("Artist Profile", upload_to = artistIcon ,)
    album_cover = models.ImageField("Album Cover",   upload_to = songsAlbum ,)             #next step store m_image and s_iamge i a seperate folder
      

    RATING_CHOICES = (
        ('5', 'Very Good'), 
        ('4', 'Good'), 
        ('3', 'Fair'),
        ('2', 'Poor'), 
        ('1', 'Very Poor'),
       
    )
    rating = models.CharField(max_length=1, choices=RATING_CHOICES)

    SONG_CHOICES = (
       ('Pop', 'Pop'), ('Rap', 'Rap'), ('Classical', 'Classical'),('Indian', 'Indian'),
       ('Instrumental','Instrumental')
       
    )
    song_type = models.CharField(max_length=20, choices=SONG_CHOICES)

    # rating = models.ChoiceField( )
    # song_type =  models.ChoiceField(('Pop', 'Pop'), ('Rap', 'Rap'), ('Classical', 'Classical'),('Indian', 'Indian') )
  

    class Meta:
         verbose_name_plural = "music"
         ordering = ['-rating']

    def __len__():
          return len(Music)
    	
    def __unicode__(self):
          return self.title