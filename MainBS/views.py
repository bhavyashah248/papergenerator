# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Teacher,Chapter,Type,Question,Subject


# Create your views here.
def index(request):
    return render(request, 'MainBS/login.html', None)


def BSform(request):
    return render(request, 'MainBS/BSform.html', None)


def Auth(request):
    uname = request.POST.get('username', '')
    pwd = request.POST.get('pwd', '')
    user = authenticate(username=uname, password=pwd)

    if user is not None:

        if user.is_active:
            login(request, user)
            return redirect('Home/', request, None)
    else:
        return render(request, 'MainBS/login.html', None)


@login_required(login_url="/MainBS")
def Home(request):
    return render(request, 'MainBS/Home.html', None)


def lout(request):
    logout(request)
    return render(request, 'MainBS/login.html', None)


def addq(request):
    teacher = Teacher.objects.get(user = request.user)
    sub = teacher.subject
    typ = Type.objects.filter(subject = sub)
    chap = Chapter.objects.filter(subject=sub)

    return render(request, 'MainBS/addq.html', {'type':typ,'chapter':chap, 'subject':sub})

def sub(request):
    try:
        teacher = Teacher.objects.get(user=request.user)
        sub = teacher.subject
        chap = str(request.POST.get('chapter', ''))
        type = str(request.POST.get('type', ''))
        marks = str(request.POST.get('marks', ''))
        quest = str(request.POST.get('question', ''))
        ans = str(request.POST.get('answer', ''))
        # fsub = Subject.objects.get(subject = sub)
        fchap = Chapter.objects.get(name = chap)
        ftype = Type.objects.get(name = type)
        que = Question(subject=sub,chapter = fchap, type = ftype, marks = marks, question = quest,q_id = 'nakami', answer = ans)
        que.save()
        return render(request, 'MainBS/success.html', {"result": que})
    except:
        return render(request, 'MainBS/fail.html', None)

    # result.append(chap)
    # result.append(type)
    # result.append(marks)
    # result.append(quest)
    # result.append(ans)



