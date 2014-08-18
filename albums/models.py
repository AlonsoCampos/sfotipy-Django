from django.db import models
from artistas.models import Artist

class Album(models.Model):
	title           = models.CharField(max_length=255)
	cover           = models.ImageField(upload_to="albums")
	artist          = models.ForeignKey(Artist)
	#favorite_songs  = models.ManytoManyField('track.Tracks', blank=True, related_name='is_favorite_of')

	def Image_Album(self):
		#return self.track_file.url
		return """
			<img src="%s" />	
		"""%self.cover.url
	Image_Album.allow_tags = True
	def __unicode__(self):
		return self.title
