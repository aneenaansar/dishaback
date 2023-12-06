from django.contrib import admin
from django.urls import path,include
from .views import login

from . import views
from .views import *

app_name = 'dashboard'

urlpatterns = [
    path('',views.login,name='login'),
    path('index/',views.index, name='index'),
   
    path('detail/',views.detail, name='detail'),
    path('appoinments/',views.appoinments, name='appoinments'),
    path('bloglist/',views.displayblog, name='bloglist'),
    path('patient_list/', PatientListView.as_view(), name='patient'),
    # path('accounts/', include('django.contrib.auth.urls')),

    path('blogs/<int:pk>/edit/', BlogEditView.as_view(), name='edit_blog'),
    path('blogs/<int:pk>/delete/', BlogDeleteView.as_view(), name='delete_blog'),
    path('logout/', views.logout_view, name='logout'),
    path('addblog/', BlogAddView.as_view(), name='addblog'),
    

]