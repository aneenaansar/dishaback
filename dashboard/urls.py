from django.contrib import admin
from django.urls import path,include
# from django.contrib.auth import views as auth_views

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
    # path('accounts/', include('django.contrib.auth.urls')),
]