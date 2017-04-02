from django.conf.urls import url
from django.contrib.auth import views as auth_views
from data import views

urlpatterns = [
    url(r'^search/$', views.download, name='search'),
    url(r'^download/$', views.download_data, name='download_data'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^list_observer/$', views.list_of_contrib),
    url(r'^upload_edit/$', views.upload_edit, name='upload_data'),
    url(r'^view_more/$', views.view_more, name='like'),
    url(r'^filter/$', views.filter, name='filter')
]
