# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login.models import Userdb
from ..companies.models import Company
from django.db import models

# Create your models here.
class ProjectManager(models.Manager):
    
    def validator(self, postData):
        errors=[]
        if not postData['project']:
            errors.append("Company id cannot be blank. Please go back to dashboard to add a new company if needed")

        return errors

    def creator(self, postData):
        return self.create(
            title = postData['title'],
            billing_code=postData['billing_code'],
            billing_rate=postData['billing_rate'],
            rate_type=postData['rate_type'],
            note=postData['note'],
            project=Company.objects.get(id=postData['project']),
        )

class Project(models.Model):
    title = models.CharField(max_length =255, blank=True)
    billing_code = models.TextField(blank=True)
    billing_rate = models.DecimalField(max_digits = 100, decimal_places=2, blank=True)
    rate_type=models.CharField(max_length = 45)
    note = models.TextField(null=True)
    users = models.ManyToManyField(Userdb, related_name="staffs")
    project = models.ForeignKey(Company, related_name="projects")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = ProjectManager()