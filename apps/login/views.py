# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from .models import Userdb
import bcrypt
# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def register(request):
    val = Userdb.objects.validator(request.POST)
    if len(val) > 0:
        for v in val:
            messages.error(request, v)
            return redirect ('/')
        
    else:
        
        messages.add_message(request, messages.INFO, "Registration success! Please log in")
        user = Userdb.objects.creator(request.POST)
        user_id = user.id
        request.session['user_id'] = user_id
        return redirect("/dashboard")
     

def login(request):
    val = Userdb.objects.check_login(request.POST)
    if len(val) > 0:
        for e in val:
            messages.error(request, e)
        return redirect("/")
        
    else:
        user = Userdb.objects.get(email=request.POST['email'])
        user_id = user.id
        request.session['user_id'] = user_id
        print request.session['user_id']
        return redirect("/dashboard") 

def logout(request):
    request.session.clear()
    return redirect ('/')

def addusers(request):
    return render(request, 'login/addusers.html')

def viewusers(request):
    context = {
        'users' : Userdb.objects.all(),
    }
    return render(request, 'login/viewusers.html', context)

def showusers(request, id):
    if request.method =="POST":
        edit = Userdb.objects.get(id=id)
        edit.first_name = request.POST['first_name']
        edit.last_name = request.POST['last_name']
        edit.email = request.POST['email']
        edit.password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        edit.save()
    context = {
        'user' : Userdb.objects.get(id=id),
    }
    return render(request, 'login/showusers.html', context)

def deleteusers(request, id):
    Userdb.objects.get(id=id).delete()
    return redirect ('/viewusers')

def usersfind(request):
    return render(request, 'login/_find.html',
        { "users": Userdb.objects.filter(first_name__startswith=request.POST['search']) }
    )

# def usersfind(request):
#     context = {
#         "users": Userdb.objects.filter(first_name__startswith=request.POST['search']) 
#     }
#     return HttpResponse(context)
