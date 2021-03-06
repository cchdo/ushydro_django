from django.conf.urls import patterns, include, url
from django.conf import settings
#from django.template import add_to_builtins
#add_to_builtins('smart_load_tag.templatetags.smart_load')

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        # Examples:
        # url(r'^$', 'ushydro.views.home', name='home'),
        # url(r'^ushydro/', include('ushydro.foo.urls')),

        url(r'^s4p/?$', 'legacy.views.redirect_s4p'),

        # Uncomment the admin/doc line below to enable admin documentation:
        # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

        # Uncomment the next line to enable the admin:
        url(r'^admin/', include(admin.site.urls)),
        #url(r'^bibliography/', include('bibliography.urls')),
        #url(r'^hydrotable/', include('hydrotable.urls')),
        url(r'^cached.json', 'bibliography.views.cached_bibliography'),
        url(r'^load.json', 'bibliography.views.load_bibliography'),
        (r'^', include('cms.urls')),
        (r'^', include('cms.urls', namespace='imagestore')),
        )

if settings.DEBUG:
    urlpatterns = patterns('',
            url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT,
                    'show_indexes': True}),
                url(r'',
                    include('django.contrib.staticfiles.urls')),
                ) + urlpatterns
