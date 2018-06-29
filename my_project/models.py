# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    userName = models.CharField(max_length=30,primary_key=True)
    userPw = models.CharField(max_length=30)