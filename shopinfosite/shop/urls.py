from django.conf.urls import url

from . import views

app_name = 'shop'

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^about$', views.about, name='about'),
    url(r'^gallery$', views.galleries, name='gallery'),
    url(r'^news$', views.news, name='news'),
    url(r'^gallery/(?P<gallery_id>[0-9]+)/$', views.view_gallery, name='view_gallery'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.view_category, name='view_category'),

]