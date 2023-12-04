from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .forms import LoginForm

from django.shortcuts import render, get_object_or_404
from django.views import View

from django.urls import reverse
from django.http import HttpResponseRedirect

def login(request):
    form = LoginForm()
    return render(request,'dashboard/login.html', {'form': form})

class BlogEditView(View):
    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        return render(request, 'dashboard/blog_edit.html', {'blog': blog})

    def post(self, request, pk):
        # Handle form submission to update the blog
        # This will depend on your specific form implementation
        # Update the blog object and save it
        return HttpResponseRedirect(reverse('dashboard:blog_list'))

class BlogDeleteView(View):
    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        return render(request, 'dashboard/blog_delete.html', {'blog': blog})

    def post(self, request, pk):
        # Handle form submission to delete the blog
        # Delete the blog object
        return HttpResponseRedirect(reverse('dashboard:blog_list'))

def index(request):
    return render(request,'dashboard/index.html')

def addblog(request):
    return render(request, 'dashboard/addblog.html')

def detail(request):
    return render(request,'dashboard/detail.html')

def appoinments(request):
    return render(request,'dashboard/appoinments.html')

def displayblog(request):
    blogs=Blog.objects.all()
    return render(request,'dashboard/displayblog.html',{'blogs':blogs})

def patient(request):
    return render(request,'dashboard/patient.html')
