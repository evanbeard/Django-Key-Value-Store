from django.conf.urls.defaults import patterns, url
import views

urlpatterns = patterns('',
    url(r'^store/$', views.store_value),
    url(r'^retrieve/$', views.retrieve_value),
                      )
