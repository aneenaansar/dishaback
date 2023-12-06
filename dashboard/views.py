from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login  # Rename login to avoid conflicts
from main.models import *
from django.contrib.auth import logout
from django.shortcuts import redirect

from django.shortcuts import render, get_object_or_404
from django.views import View
from .forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

class BlogAddView(View):
    template_name = 'dashboard/addblog.html'

    def get(self, request):
        form = BlogForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = BlogForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('dashboard:bloglist')  # Adjust the URL name as needed
        else:
            return render(request, self.template_name, {'form': form})

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
            return redirect('dashboard:bloglist')
        else:
            # If the form is not valid, re-render the page with the form and errors
            return render(request, self.template_name, {'blog': blog, 'form': form})
class BlogDeleteView(View):
    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        blog.delete()
        return redirect('dashboard:bloglist')

def index(request):
    return render(request,'dashboard/index.html')

def addblog(request):
    return render(request,'dashboard/addblog.html')

def detail(request):
    return render(request,'dashboard/detail.html')

def appoinments(request):
    appoinments=Appointment.objects.all()
    return render(request,'dashboard/appoinments.html',{'appoinments':appoinments})

def displayblog(request):
    blogs=Blog.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(blogs, 10)  # Show 10 tasks per page

    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    return render(request,'dashboard/blog_list.html',{'blogs':blogs})

def patient(request):
    return render(request,'dashboard/patient.html')


def logout_view(request):
    logout(request)
    # Redirect to a specific URL after logout, or to the homepage
    return redirect('dashboard:login')    
