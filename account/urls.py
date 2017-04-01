from django.conf.urls import url
from django.contrib.auth.views import logout, logout_then_login
from .views import register, user_login
urlpatterns = [
    # post views
    url(r'^login/$', user_login, name='login'),
    url(r'^logout/$', logout, {'template_name':'account/logout.html'} , name='logout'),
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),
    url(r'^register/$', register, name='register'),
    # url(r'^profile/$', profile, name='profile')
]

'''
login logout coming from templates/registration/ since i am using native auth views
though in views i am rendering account/login
again in register i am using custom so here from templates/account/
'''