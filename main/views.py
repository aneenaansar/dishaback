from django.shortcuts import render,redirect, get_object_or_404
from .models import Blog
from . forms import AppointmentForm
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.

def index(request):
    form=AppointmentForm()
    return render(request,'index.html', {'form':form})

def consult(request):
    form=AppointmentForm()
    return render(request, 'consult.html',{'form':form})

def about(request):
    form=AppointmentForm()
    return render(request, 'about.html',{'form':form})

def blog(request):
    form=AppointmentForm()
    blogs = Blog.objects.order_by('-date')[:6]
    return render(request, 'blog.html',{'form':form,
        'blogs' : blogs,
    })

def single(request,pk):
    form=AppointmentForm()
    # blog =Singleblog.objects.get(pk=pk)
    blog=Blog.objects.get(pk=pk)
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'like':
            blog.likes += 1
        elif action == 'share':
            blog.shares += 1

        blog.save()

        # Return updated counts as JSON
        return JsonResponse({'likes': blog.likes, 'shares': blog.shares})

    return render(request, 'single.html',{'form':form,
        'blog' : blog,
        # 'blogs':blogs
    })


def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Appointment request has been sent.')
        else:
            messages.error(request, 'Sorry, Your Appointment request has some errors')
    else:
        form = AppointmentForm()

    return render(request, 'index.html', {'form': form})

