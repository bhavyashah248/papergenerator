# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BUA
from MainBS.models import Teacher
from django.contrib import admin
from .models import Question, Subject, Type, Chapter

admin.site.register(Question)
admin.site.register(Subject)
admin.site.register(Type)
admin.site.register(Chapter)


class TeacherInline(admin.StackedInline):
    model = Teacher
    can_delete = False
    verbose_name_plural = 'teacher'


class UserAdmin(BUA):
    inlines = (TeacherInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
