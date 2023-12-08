from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField(null=True)
    age = models.IntegerField(max_length=150)
    patient_id = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    date = models.DateField(null=True)
    remarks = models.TextField(null=True)

class Remark(models.Model):
    patient = models.ForeignKey(Patient, related_name='patient_remarks', on_delete=models.CASCADE)
    date = models.DateField(null=True)
    remarks = models.TextField(null=True)