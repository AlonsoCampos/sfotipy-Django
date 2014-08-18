from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()
#Se toma de views
from artistas.views import ArtistDetailView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'curso.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #   (r'^grappelli/', include('grappelli.urls')), # grappelli URLS	
    url(r'^tracks/(?P<title>[\w\-\W]+)/', 'track.views.track_view', name='track_view'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/','userprofiles.views.signup', name='signup'),
 	url(r'^singin/','userprofiles.views.singin', name='singin'),
    url(r'^artists/(?P<pk>[\d]+)',ArtistDetailView.as_view()),
      
)

urlpatterns += patterns('',
	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
)
