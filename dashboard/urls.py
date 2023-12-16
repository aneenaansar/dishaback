from django.contrib import admin
from django.urls import path,include


from . import views
from .views import *

app_name = 'dashboard'

urlpatterns = [
    path('',views.login,name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('index/',views.index, name='index'),
   
    
    path('appoinments/',views.appoinments, name='appoinments'),
    path('appointmentedit/<int:pk>',AppointmentEditView.as_view(), name='appointmentedit'),
    path('appoinments/<int:pk>/delete/', AppointmentDeleteView.as_view(), name='delete_appointment'),

   
    path('patient_list/', PatientListView.as_view(), name='patient'),
    path('patient_list/<int:pk>/delete/', PatientDeleteView.as_view(), name='delete_patient'),
    path('patient_details/', PatientDetailsView.as_view(), name='patient_details'),
    path('patient_edit/<int:patient_id>/', PatientEditView.as_view(), name='patient_edit'),

    path('addblog/', BlogAddView.as_view(), name='addblog'),
    path('bloglist/',views.displayblog, name='bloglist'),
    path('blog/edit/<int:pk>/', BlogEditView.as_view(), name='blog_edit'),
    path('blogs/<int:pk>/delete/', BlogDeleteView.as_view(), name='delete_blog'),

    path('review/',views.review, name='review'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='delete_review'),


    
    
    

]