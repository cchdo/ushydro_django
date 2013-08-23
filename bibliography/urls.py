from django.conf.urls import patterns, url

from bibliography import views

urlpatterns = patterns('',
        url(r'^$', views.index, name="index"),
        url(r'^cached.json$', views.cached_bibliography, name="cached"),
        url(r'^load.json$', views.load_bibliography, name="load"),
        )
