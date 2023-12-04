from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login  # Rename login to avoid conflicts
from main.models import *

from django.shortcuts import render, get_object_or_404
from django.views import View
from .forms import *
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Use the renamed function
            # Redirect to the admin dashboard or any other page
            return redirect('dashboard:index')  # Replace 'dashboard:index' with your actual dashboard URL
        else:
            # Handle invalid login credentials
            return render(request, 'dashboard/login.html', {'error': 'Invalid username or password'})
    return render(request, 'dashboard/login.html')

class BlogEditView(View):
    template_name = 'dashboard/edit.html'

    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        return render(request, self.template_name, {'blog': blog})

    def post(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)

        # Create a form instance and populate it with data from the request
        form = BlogForm(request.POST, request.FILES, instance=blog)

        # Check if the form is valid
        if form.is_valid():
            # Save the form to update the blog
            form.save()
            return redirect('dashboard:displayblog')
        else:
            # If the form is not valid, re-render the page with the form and errors
            return render(request, self.template_name, {'blog': blog, 'form': form})
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
    return render(request,'dashboard/addblog.html')

def detail(request):
    return render(request,'dashboard/detail.html')

def appoinments(request):
    return render(request,'dashboard/appoinments.html')

def displayblog(request):
    blogs=Blog.objects.all()
    return render(request,'dashboard/displayblog.html',{'blogs':blogs})

def patient(request):
    return render(request,'dashboard/patient.html')
