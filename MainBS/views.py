# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> This is our homepage </h1>")

def BSform(request):
    return render(request,'MainBS/BSform.html',None)


# Create your views here.
