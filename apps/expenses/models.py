# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..login.models import Userdb
from ..companies.models import Company
from ..projects.models import Project


class ReportManager(models.Manager):
    def creator(self,postData):
        return self.create(
            name = postData['name'],
            period = postData['period'],
            admin = Userdb.objects.get(id=postData['admin']),
        )

class Report(models.Model):
    name = models.CharField(max_length = 255)
    period = models.DateField()
    admin = models.ForeignKey(Userdb, related_name="comps")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReportManager()

class Expense(models.Model):
    date = models.DateField(auto_now=False)
    category = models.CharField(max_length = 255)
    vendor = models.CharField(max_length = 255)
    desc = models.TextField(null=True, blank=True)
    image = models.FileField(null=True, blank=True, upload_to="documents/")
    amount = models.DecimalField(max_digits=100, decimal_places = 2, null=True, blank=True)
    record = models.ForeignKey(Report, related_name="records")
    job = models.ForeignKey(Project, related_name="sites")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
