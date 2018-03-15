# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=30)
    chapter = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    marks = models.CharField(max_length=10)
    question = models.CharField(max_length=200)
    q_id = models.CharField(max_length=20)
    answer = models.CharField(max_length=500)
