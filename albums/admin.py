from django.contrib import admin
from .models import Album

class AlbumAdmin(admin.ModelAdmin):
	list_display = ('title','Image_Album')

admin.site.register(Album,AlbumAdmin)

# Register your models here.
