from django.contrib import admin
from django.urls import path,include
from .views import superuser_login

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('',views.login,name='login'),
    path('index/',views.index, name='index'),
    path('addblog/',views.addblog, name='addblog'),
    path('detail/',views.detail, name='detail'),
    path('appoinments/',views.appoinments, name='appoinments'),
    path('displayblog/',views.displayblog, name='displayblog'),
    path('patient/', views.patient, name='patient'),
    path('superuser-login/', superuser_login, name='superuser_login'),
]