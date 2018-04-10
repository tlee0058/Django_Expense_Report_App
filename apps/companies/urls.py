from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^addcompanies$', views.addcompanies),
    url(r'^addcompaniesdata$', views.addcompaniesdata),
    url(r'^viewcompanies$', views.viewcompanies),
    url(r'^showcompanies/(?P<id>\d+)$', views.showcompanies),
    url(r'^companies/delete/(?P<id>\d+)$', views.deletecompanies),
    
   
]