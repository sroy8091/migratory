from django.conf.urls import url
from django.contrib.auth import views as auth_views
from data import views

urlpatterns = [
    url(r'^search/$', views.download, name='search'),
    url(r'^download/$', views.download_data, name='download_data'),
    url(r'^upload/$', views.upload, name='upload'),
]
