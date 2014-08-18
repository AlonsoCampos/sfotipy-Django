
#Se agrega en los settings para poder utulizar 
#el nombre de la carpeta y la funcion
#
#from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
#TEMPLATE_CONTEXT_PROCESSORS = TCP + (
#    'curso.context_processors.basico'
#)

#Aqui me permite enviar mensajes aleatorios a una variable
# llamada titulo 
#from random import choice

#frases = ['lol','hola','Yoshi','verde']

#def basico(request):
#    return {'titulo':choice(frases)}


from random import choice
from track.models import Tracks

frases = ['lol','hola','Yoshi','verde']
# Se importan las canciones

def basico(request):
	tracks = Tracks.objects.all()
	track = None 
	for t in tracks:
		if request.path == t.get_absolute_url():
			track = t
			break
	return {'titulo':choice(frases),'trac':tracks,'selected_track':track}
