from django.contrib import admin
from django.urls import path,include
# from django.contrib.auth import views as auth_views

from . import views
from .views import BlogEditView, BlogDeleteView

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

    path('blogs/<int:pk>/edit/', BlogEditView.as_view(), name='edit_blog'),
    path('blogs/<int:pk>/delete/', BlogDeleteView.as_view(), name='delete_blog'),
]