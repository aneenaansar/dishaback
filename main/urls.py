from django.contrib import admin
from django.urls import path,include

from . import views

app_name = 'main'

urlpatterns = [
    path("",views.index,name='index'),
    path('consult/',views.consult, name='consult'),
    path('about/',views.about, name='about'),
    path('blog/',views.blog, name='blog'),
    path('single/<int:pk>/',views.single, name='single'),
    path('appointment/', views.appointment, name='appointment'),
    
]