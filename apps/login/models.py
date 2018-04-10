# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z]{2,}$')
PASSWORD_REGEX = re.compile(r'^.{8,}$')


# Create your models here.
class UserdbManager(models.Manager):
    def validator(self, postData):
        errors=[]
        if not EMAIL_REGEX.match(postData['email']):
            errors.append("Invalid Email")
        else: 
            query = self.filter(email = postData['email']).first()
            if query > 0:
                errors.append("Email exists, please log in")

        if len(postData['first_name']) < 0 or len(postData['last_name']) < 0:
            errors.append("First Name or Last name cannot be blank")

        if not PASSWORD_REGEX.match(postData['password']):
            errors.append("Password must be at least 8 characters")

        if postData['password'] != postData['confirm_pw']:
            errors.append("Password do not match")
        
        
        return errors

    def creator(self, cleanData):
        hashed_pw = bcrypt.hashpw(cleanData['password'].encode(), bcrypt.gensalt())
        return self.create(
            first_name = cleanData['first_name'],
            last_name = cleanData['last_name'],
            email = cleanData['email'],
            password = hashed_pw,
        )

    def check_login(self, loginData):
        errors = []

        if not self.filter(email = loginData['email']):
            errors.append("Invalid Login")
        else:
            dbpw = self.get(email=loginData['email']).password.encode()
            user_pw = loginData['password'].encode()         

            if not bcrypt.checkpw(user_pw, dbpw):
                errors.append("invalid password")
            

        return errors

class Userdb(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length =255, unique=True)
    password = models.CharField(max_length =255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserdbManager()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
