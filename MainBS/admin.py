# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Question, Subject, Type, Chapter

admin.site.register(Question)
admin.site.register(Subject)
admin.site.register(Type)
admin.site.register(Chapter)