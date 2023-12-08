from django import forms
from main.models import Blog
from ckeditor.fields import RichTextField
from . models import *

class BlogForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    class Meta:
        model = Blog
        fields = ['date', 'title', 'content', 'image']
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
      

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
