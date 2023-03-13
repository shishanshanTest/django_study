from django.urls import path, include
from django.http.response import HttpResponse
from . import views

app_name = 'zuoye'
urlpatterns = [
    path('', views.zuoye, name='zuoye_index'),
    path('index/', views.index, name='inxex')
]
