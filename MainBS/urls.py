from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'Register/^$', views.UserFormView.as_view(), name='register'),
    url(r'^BSform/$', views.BSform, name='BSform'),
]