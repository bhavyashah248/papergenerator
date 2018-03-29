# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from .form import UserForm




# Create your views here.
def index(request):
    return render(request, 'MainBS/login.html', None)

def BSform(request):
    return render(request,'MainBS/BSform.html',None)

class UserFormView(View):
    form_class = UserForm
    template_name = 'MainBS/Login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            username =form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.username = username
            user.set_password(password)
            user.save()

            #login user
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return render(request, "Hello")

        return render(request, self.template_name, {'form':form})