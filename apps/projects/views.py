# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from ..login.models import Userdb
from ..companies.models import Company
from .models import Project
from django.contrib import messages

# Create your views here.
def addprojects(request):
    context = {
        'companys' : Company.objects.all(),
    }
    return render(request, 'projects/addprojects.html', context)

def addprojectsdata(request):
    val = Project.objects.validator(request.POST)
    if len(val) > 0:
        for e in val:
            messages.error(request, e)
    else:
        Project.objects.creator(request.POST)
        messages.add_message(request, messages.INFO, "Project is added")

    return redirect ('/addprojects')

def viewprojects(request):
    context = {'projects': Project.objects.all(),}
    return render(request, 'projects/viewprojects.html', context)
