from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from rawApi import views

urlpatterns = patterns(
    'rawApi.views',
    url(r'^tasks/$', 'task_list', name='task_list'),
    url(r'^tasks/(?P<pk>[0-9]+)$', 'task_detail', name='task_detail'),
   	url(r'^zip_list/$', views.ZipList.as_view(),name='zip-list'),
    url(r'^zip_create/$', views.ZipCreate.as_view(),name='zip-list'),
    url(r'^zip/(?P<pk>[0-9]+)/$', views.ZipDetail.as_view(),name='zip-detail'),
    url(r'^state/$', views.StateList.as_view(),name='state-list'),
    url(r'^state/(?P<pk>[0-9]+)/$', views.StateDetail.as_view(),name='state-detail'),
    url(r'^country/$', views.CountryList.as_view(),name='country-list'),
    url(r'^country/(?P<pk>[0-9]+)/$', views.CountryDetail.as_view(),name='country-detail'),
    url(r'^city/$', views.CityList.as_view(),name='city-list'),
    url(r'^city/(?P<pk>[0-9]+)/$', views.CityDetail.as_view(),name='city-detail'),
)


urlpatterns = format_suffix_patterns(urlpatterns)