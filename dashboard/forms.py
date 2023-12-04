
from django import forms
from django import forms
from main.models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['date', 'heading', 'paragraph', 'image', 'h1', 'p1', 'h2', 'p2', 'h3', 'p3', 'p4', 'p5']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
