from django.contrib import admin
from .models import Artist
from track.models import Tracks
from albums.models import Album

class TrackInline(admin.StackedInline):
	model = Tracks
	extra = 1

class AlbumInline(admin.StackedInline):
	model = Album
	extra = 1
#Extra me permite controlar el numeor de 
#registros a manipular
class AdminArtist (admin.ModelAdmin):
	list_display  = ('first_name','last_name','biography')
	search_fields = ('first_name','last_name')
	inlines 	  = [TrackInline,AlbumInline]
# Me permite editar los registros relacionados
# del registro de Artistas
# 
admin.site.register(Artist,AdminArtist)

