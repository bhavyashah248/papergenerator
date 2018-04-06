import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","BSProject.settings")
django.setup()
from MainBS.models import Subject

# sub = Subject.objects.all()
# for each in sub:
#     print(each.value)

def algo (marks = 0,type = [], chap = []):
    return "real BS"