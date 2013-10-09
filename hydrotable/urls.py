from django.conf.urls import patterns, url

from hydrotable import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^custom/$', views.custom, name='custom'),
        url(r'^custom/step2/$', views.step2, name='step2'),
        url(r'^custom/build/$', views.build, name='build')
    )
