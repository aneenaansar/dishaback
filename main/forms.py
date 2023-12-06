from django import forms
from .models import Appointment

TIME = (
    ('Morning' , 'Morning'),
    ('Evening' , 'Evening'),
)



class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'contact', 'purpose', 'date', 'time']

    name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'border border-gray-800 rounded p-2 w-full'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'border border-gray-800 rounded p-2 w-full'}))
    contact = forms.CharField(widget=forms.TextInput(attrs={'class': 'border border-gray-800 rounded p-2 w-full'}))
    purpose = forms.CharField(widget=forms.TextInput(attrs={'class': 'border border-gray-800 rounded p-8 w-full'}))
    date = forms.DateField(widget=forms.TextInput(attrs={'class': 'border border-gray-800 rounded p-2 w-full','type': 'date'}))
    time = forms.CharField(widget=forms.Select(choices=TIME,attrs={'class': 'border border-gray-800 rounded p-2 w-full'}))

