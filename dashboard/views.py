from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'dashboard/login.html')

def index(request):
    return render(request,'dashboard/index.html')

def addblog(request):
    return render(request,'dashboard/addblog')

def detail(request):
    return render(request,'dashboard/detail.html')

def appoinments(request):
    return render(request,'dashboard/appoinments.html')

def displayblog(request):
    return render(request,'dashboard/displayblog.html')

def patient(request):
    return render(request,'dashboard/patient.html')
