# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from ..login.models import Userdb
from ..expenses.models import Expense, Report
from ..projects.models import Project
from time import gmtime, strftime, localtime

# Create your views here.
def dashboard(request):
    context = {
        'user' : Userdb.objects.get(id=request.session['user_id']),
        'reports' : Report.objects.filter(admin=Userdb.objects.get(id=request.session['user_id'])),
        'projects' : Project.objects.all(),
        "time": strftime("%B %d, %Y %I:%M %p", localtime())
    
    }
    return render(request, 'dashboard/dashboard.html', context)

def view_report(request, id):
    context = {
        'report' : Report.objects.get(id=id),
        'expenses' : Expense.objects.filter(record=Report.objects.get(id=id)),
    }
    return render(request, 'dashboard/viewreports.html', context)