from django.urls import path, include
from django.http.response import HttpResponse
from . import views

app_name = 'zuoye'
urlpatterns = [
    path('', views.zuoye, name='zuoye_index'),
    path('index/', views.index, name='inxex'),
    path('index1/', views.index1, name='inxex1'),
    path('index2/', views.index2, name='index2'),
    path('index3/', views.index3, name='index3'),
    path('index4/', views.index4, name='index4'),
    path('index5/', views.index5, name='index5'),
    path('index6/', views.index6, name='index6'),
    path('index7/', views.index7, name='index7'),
]
