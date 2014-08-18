from django.contrib import admin
from .models import Tracks

class TrackAdmin(admin.ModelAdmin):
	list_display  = ('id','title','es_pharrel','artist','order','albums','player')
#Se le pasa como parametro la clase creada
#para poder mostrar campos o atributos del modelo
	list_filter   = ('artist','albums',)
#Me permite crear un apartado de filtro atravez de los
#campos que se pasen en la tupla de arriba
	search_fields = ('title','artist__first_name','albums__title')
#Me permite realizar busquedas atravez de los campos
#contenidos en la tupla
#Pasando artist__first_name 
#artist es el nombre de la llave foranea
#__first_name me permite acceder a los atributos de esa
#llave foranea por eso se usa asi artist__first_name
	def es_pharrel(self,obj):
		return obj.id ==1
	es_pharrel.boolean = True
#Me permite crear un icono en vez de devolver
#True o False
	list_editable = ('title','albums')
#Si colocamos el primer campo de la vista marca error a 
#a menos que especifiquemos que campos van a terner enlaces
	raw_id_fields = ('artist',)
#Me permite crear una ventana nueva que me permite buscar
#elementos si se modifica el modulo de Artista
# de esta manera nos permitira hacer una busqueda mas
#mas personalizada
#
#class AdminArtist (admin.ModelAdmin):
#	list_display = ('first_name','last_name','biography')
#	search_fields = ('first_name','last_name')
	

admin.site.register(Tracks, TrackAdmin)
