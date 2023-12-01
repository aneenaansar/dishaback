from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

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

@user_passes_test(lambda u: u.is_superuser)
def superuser_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard or any other page
        else:
            # Handle authentication failure
            return render(request, 'your_login_template.html', {'error_message': 'Invalid credentials'})

    return render(request, 'your_login_template.html')


