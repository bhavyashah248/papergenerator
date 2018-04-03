# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




class Chapter(models.Model):
    name = models.CharField(max_length=30)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=30)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Question(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    marks = models.CharField(max_length=10)
    question = models.CharField(max_length=200)
    q_id = models.CharField(max_length=20)
    answer = models.CharField(max_length=500)

    def __str__(self):
        return self.q_id




