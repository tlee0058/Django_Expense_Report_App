from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^addexpenses$', views.addexpenses),
    url(r'^addreport$', views.addreport),
    url(r'^addreceipt/(?P<id>\d+)$', views.addreceipt),
    url(r'^report/reset$', views.report_reset),
    url(r'^project/summary/(?P<id>\d+)$', views.projectsummary),
    
]
