from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^addprojects$', views.addprojects),
    url(r'^addprojectsdata$', views.addprojectsdata),
    url(r'^viewprojects$', views.viewprojects),

]
