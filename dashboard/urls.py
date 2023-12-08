from django.contrib import admin
from django.urls import path,include


from . import views
from .views import *

app_name = 'dashboard'

urlpatterns = [
    path('',views.login,name='login'),
    path('index/',views.index, name='index'),
   
    path('patient_details/', PatientDetailsView.as_view(), name='patient_details'),
    path('appoinments/',views.appoinments, name='appoinments'),
    path('appointmentedit/<int:pk>',AppointmentEditView.as_view(), name='appointmentedit'),
    path('appoinments/<int:pk>/delete/', AppointmentDeleteView.as_view(), name='delete_appointment'),
    path('bloglist/',views.displayblog, name='bloglist'),
    path('patient_list/', PatientListView.as_view(), name='patient'),
    path('patient_list/<int:pk>/delete/', PatientDeleteView.as_view(), name='delete_patient'),

    path('blog/edit/<int:pk>/', BlogEditView.as_view(), name='blog_edit'),
    path('blogs/<int:pk>/delete/', BlogDeleteView.as_view(), name='delete_blog'),
    path('logout/', views.logout_view, name='logout'),
    path('addblog/', BlogAddView.as_view(), name='addblog'),
    

]