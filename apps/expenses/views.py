# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from ..login.models import Userdb
from ..companies.models import Company
from ..projects.models import Project
from .models import Report, Expense
from django.contrib import messages
from django.core import serializers
import json

def addexpenses(request):
    if 'reportID' not in request.session:
        request.session['reportID'] = None

    context = {
        'projects' : Project.objects.all(),
        'count' : Project.objects.all().count(),
        'users' : Userdb.objects.all(),
        'reportID' : request.session['reportID'],
        'receipts' : Expense.objects.filter(record = request.session['reportID']),
        'count' : Report.objects.filter(admin=request.session['user_id']).count(),
        
    }
    
    return render(request, 'expenses/addexpenses.html', context)

def addreport(request):
    
    print request.POST

    new_report = Report.objects.creator(request.POST)
    request.session['reportID'] = new_report.id
    
    # context = {
    #     'reportID' : request.session['reportID'],
    #     'users' : Userdb.objects.all(),
    #     'projects' : Project.objects.all(),
    # }
    print request.session['reportID']
    return redirect ('/addexpenses')

def addreceipt(request, id):


    Expense.objects.create(
        date = request.POST['date'],
        category = request.POST['category'],
        vendor = request.POST['vendor'],
        desc = request.POST['desc'],
        amount = request.POST['amount'],
        record = Report.objects.get(id=id),
        job = Project.objects.get(id=request.POST['job']),
        image = request.FILES['image'],
        
    )

    return redirect ('/addexpenses')

def report_reset(request):
    request.session['reportID'] = None
    return redirect ('/dashboard')

def projectsummary(request,id):
    context = {
        'project' : Project.objects.get(id=id),
    }

    return render(request, 'expenses/viewprojects.html', context)