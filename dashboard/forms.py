from django import forms
from main.models import Blog
from ckeditor.fields import RichTextField

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
      

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
