import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Tracks
from .models import Album

#@login_required
def track_view(request,title):
	#import ipdb; ipdb.set_trace()
	track = get_object_or_404(Tracks, title=title)
	bio   = track.artist.biography

	data  = {
		'title' : track.title,
		'order' : track.order,
		'album' : track.albums.title,
		'artist': {
			'name' : track.artist.first_name,
			'bio'  : bio,
		}
	}
	#Esto es una serializacion con JSON
	#Se puede hacer con XML y ARRAYS
	#json_data = json.dumps(data) #Convierte la informacion en json
	#return HttpResponse(json_data,content_type="application/json");
	return render(request,'track.html',{'track':track})
