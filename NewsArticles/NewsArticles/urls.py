
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin





urlpatterns = patterns('',

    url(r'^article/' , include('articles.urls')),
    url(r'^admin/', include(admin.site.urls)),
	)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT, 'show_indexes': True
    }),
)	
  
if settings.DEBUG:
    urlpatterns += patterns(
		'django.views.static',
		(r'media/(?P<path>.*)',
		'serve',
		{'document_root': settings.MEDIA_ROOT}),)
		
   