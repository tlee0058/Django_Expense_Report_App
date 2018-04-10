# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login.models import Userdb
from django.db import models



# Create your models here.
class CompanyManager(models.Manager):
    def validator(self, postData):
        errors=[]
        if self.filter(name=postData['name']):
            errors.append("Company is already in the system")
        elif postData['name'].islower():
            errors.append("First character of the Company name must be in Uppercase")
        return errors




    def creator(self, postData):
        return self.create(
        name=postData['name'],
        address=postData['address'],
        city=postData['city'],
        state=postData['state'],
        zip_code=postData['zip_code'],
        phone=postData['phone'],
        email=postData['email'],
        fax=postData['fax'],
        website=postData['website'],
        taxid=postData['taxid'],

        )
    

class Company(models.Model):
    name = models.CharField(max_length = 255, blank=True, null=True)
    address = models.CharField(max_length = 255, blank=True, null=True)
    city=models.CharField(max_length = 100, blank=True, null=True)
    state = models.CharField(max_length = 2, blank=True, null=True)
    zip_code = models.TextField(max_length = 10, blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length = 20, blank=True, null=True)
    website = models.CharField(max_length = 255, blank=True, null=True)
    taxid = models.CharField(max_length = 20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = CompanyManager()

