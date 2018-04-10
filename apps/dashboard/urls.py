from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard$', views.dashboard),
    url(r'^view/report/(?P<id>\d+)$', views.view_report),
   
]