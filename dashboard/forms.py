
from django import forms
from django import forms
from main.models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','content','image','date']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
