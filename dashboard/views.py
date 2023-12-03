from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .forms import LoginForm

# Create your views here.
def login(request):
    form = LoginForm()
    return render(request,'dashboard/login.html', {'form': form})

def index(request):
    return render(request,'dashboard/index.html')

def addblog(request):
    return render(request, 'dashboard/addblog.html')

def detail(request):
    return render(request,'dashboard/detail.html')

def appoinments(request):
    return render(request,'dashboard/appoinments.html')

def displayblog(request):
    return render(request,'dashboard/displayblog.html')

def patient(request):
    return render(request,'dashboard/patient.html')
