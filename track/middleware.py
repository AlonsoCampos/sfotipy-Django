#Con esto puedo alterar el comportamiento 
#global de nuestro sitio
#Se debe de colocar en Settins la carpeta, archivo y clase
#MIDDLEWARE_CLASSES = (
#    'django.contrib.sessions.middleware.SessionMiddleware',
#    'django.middleware.common.CommonMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
#    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'django.contrib.messages.middleware.MessageMiddleware',
#    'django.middleware.clickjacking.XFrameOptionsMiddleware',
#    'track.middleware.PaisMiddleware',
#)

from random import choice
from django.shortcuts import redirect
paises = ['Colobia','Peru','Mexico']


def de_donde_vengo(request):
	return choice(paises)

class PaisMiddleware():
	def process_request(self,request):
		pais = de_donde_vengo(request)
		if pais == 'Mexico':
			return redirect('http://mejorando.la')