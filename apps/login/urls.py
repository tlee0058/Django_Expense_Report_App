from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^addusers$', views.addusers),
    url(r'^viewusers$', views.viewusers),
    url(r'^showusers/(?P<id>\d+)$', views.showusers),
    url(r'^users/delete/(?P<id>\d+)$', views.deleteusers),
    url(r'^users/find$', views.usersfind),
]
