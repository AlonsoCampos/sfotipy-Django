#Class Base Views
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Artist
#El nombre de esta clase se coloca en URLS
# para la configuracion y para que se muestre en el 
#navegador
class ArtistDetailView(DetailView):
	model = Artist
	context_object_name = 'artist'
	def get_template_names(self):
		return 'artista.html'
