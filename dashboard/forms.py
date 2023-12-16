from django import forms
from main.models import *
from ckeditor.fields import RichTextField
from . models import *

class BlogForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    class Meta:
        model = Blog
        fields = ['date', 'title', 'content', 'image','is_featured']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'ckeditor'}),
            
        }
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class RemarkForm(forms.ModelForm):
    class Meta:
        model = Remark
        fields = ['date','remarks']
# RemarkFormSet = forms.modelformset_factory(Remark, form=RemarkForm, extra=1)    
      
class PatientEditForm(forms.ModelForm):
    class Meta:
        model = Remark
        fields = ['date','remarks']


class AppointmentEditForm(forms.ModelForm):
    TIME_CHOICES = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
    ]
    STATUS = (
    ('Scheduled','Scheduled'),
    ('Pending', 'Pending'),
    ('Canceled','Canceled'),
    )

    # name = forms.CharField(widget=forms.TextInput(attrs={'class': 'border border-gray-800 rounded p-2 w-full'}))
    # email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'border border-gray-800 rounded p-2 w-full'}))
    # contact = forms.CharField(widget=forms.TextInput(attrs={'class': 'border border-gray-800 rounded p-2 w-full'}))
    # purpose = forms.CharField(widget=forms.TextInput(attrs={'class': 'border border-gray-800 rounded p-8 w-full'}))
    # date = forms.DateField(widget=forms.TextInput(attrs={'class': 'border border-gray-800 rounded p-2 w-full', 'type': 'date'}))
    # time = forms.ChoiceField(choices=TIME_CHOICES, widget=forms.Select(attrs={'class': 'border border-gray-800 rounded p-2 w-full'}))
    status= forms.ChoiceField(choices=STATUS, widget=forms.Select(attrs={'class': 'border border-gray-800 rounded p-2 w-full'}))
    class Meta:
        model = Appointment
        fields =['status']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
