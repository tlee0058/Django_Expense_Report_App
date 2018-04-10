# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from ..login.models import Userdb
from .models import Company
from django.contrib import messages
# Create your views here.
def addcompanies(request):

    return render(request, 'companies/addcompanies.html')

def addcompaniesdata(request):

    val = Company.objects.validator(request.POST)
    if len(val) >0:
        for e in val:
            messages.error(request, e)

    else:
        print request.POST
        Company.objects.creator(request.POST)
        messages.add_message(request, messages.INFO, "Company is added")

    return redirect ('/addcompanies')

def viewcompanies(request):
    context={
        'companies' : Company.objects.all().order_by('name'),
    }
    return render(request, "companies/viewcompanies.html", context)

def showcompanies(request, id):
    if request.method=="POST":

        record = Company.objects.get(id=id)
        record.name=request.POST['name']
        record.address=request.POST['address']
        record.city=request.POST['city']
        record.state=request.POST['state']
        record.zip_code=request.POST['zip_code']
        record.phone=request.POST['phone']
        record.email=request.POST['email']
        record.fax=request.POST['fax']
        record.website=request.POST['website']
        record.taxid=request.POST['taxid']
        record.save()
        messages.add_message(request, messages.INFO, "Profile is successfully edited")

    context = {
        'company' : Company.objects.get(id=id),
    }
    return render(request, 'companies/showcompanies.html', context)

def deletecompanies(request, id):
    Company.objects.get(id=id).delete()
    return redirect ('/viewcompanies')
