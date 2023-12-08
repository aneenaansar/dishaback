from django.contrib import admin
from .models import *
class RemarkInline(admin.TabularInline):
    model = Remark
    extra = 1  # Number of inline forms to display

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'patient_id', 'gender', 'address', 'phone_number', 'date', 'remarks']
    inlines = [RemarkInline]

@admin.register(Remark)
class RemarkAdmin(admin.ModelAdmin):
    list_display = ['patient', 'date', 'remarks']