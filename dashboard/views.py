from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login  # Rename login to avoid conflicts
from main.models import *
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import *
from django.shortcuts import render, get_object_or_404
from django.views import View
from .forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from main.forms import *

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
        form = BlogForm(instance=blog)
        return render(request, self.template_name, {'form': form, 'blog': blog})

    def post(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        form = BlogForm(request.POST, request.FILES, instance=blog)

        if form.is_valid():
            form.save()
            return redirect('dashboard:bloglist')
        
        return render(request, self.template_name, {'blog': blog, 'form': form})
    

class BlogDeleteView(View):
    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        blog.delete()
        return redirect('dashboard:bloglist')

class PatientDeleteView(View):
    def get(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        patient.delete()
        return redirect('dashboard:patient')
    
class PatientListView(View):
    template_name = 'dashboard/patient.html'

    def get(self, request):
        search_term = request.GET.get('search', '')
        patients = Patient.objects.all()

        if search_term:
            patients = patients.filter(
                Q(patient_id__icontains=search_term) |
                Q(first_name__icontains=search_term) |
                Q(last_name__icontains=search_term) |
                Q(phone_number__icontains=search_term)
            )

        # Pagination
        page = request.GET.get('page')
        paginator = Paginator(patients, 10)  # Show 10 patients per page

        try:
            patients = paginator.page(page)
        except PageNotAnInteger:
            patients = paginator.page(1)
        except EmptyPage:
            patients = paginator.page(paginator.num_pages)

        context = {'patients': patients}
        return render(request, self.template_name, context)

    
class PatientDetailsView(View):
    template_name = 'dashboard/patient_detail.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        # Process the main patient details
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        patient_id = request.POST.get('patientId')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        phone_number = request.POST.get('phoneNumber')
        date_of_birth = request.POST.get('dob')
        date = request.POST.get('date')
        remarks = request.POST.get('remarks')

        # Create Patient instance
        patient = Patient.objects.create(
            first_name=first_name,
            last_name=last_name,
            patient_id=patient_id,
            gender=gender,
            address=address,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
        )

        # Create Remark instance
        Remark.objects.create(
            patient=patient,
            date=date,
            remarks=remarks,
        )

        # Process dynamic fields
        dynamic_dates = request.POST.getlist('Date')
        dynamic_remarks = request.POST.getlist('Remarks')

        for dynamic_date, dynamic_remark in zip(dynamic_dates, dynamic_remarks):
            Remark.objects.create(
                patient=patient,
                date=dynamic_date,
                remarks=dynamic_remark,
            )

        return redirect('dashboard:patient')
class PatientEditView(View):
    template_name = 'dashboard/patient_edit.html'

    def get(self, request, patient_id, *args, **kwargs):
        patient = get_object_or_404(Patient, pk=patient_id)
        remarks = Remark.objects.filter(patient=patient)

        context = {
            'patient': patient,
            'remarks': remarks,
        }

        return render(request, self.template_name, context)

    def post(self, request, patient_id, *args, **kwargs):
        patient = get_object_or_404(Patient, pk=patient_id)
        remarks = Remark.objects.filter(patient=patient)

        form = PatientEditForm(request.POST, instance=patient)

        if form.is_valid():
            print("Form is valid")  # Add this line for debugging
            form.save()

            # Update remarks
            for remark in remarks:
                remark.date = request.POST.get(f'date_{remark.id}')
                remark.remarks = request.POST.get(f'remarks_{remark.id}')
                remark.save()

            print("Redirecting...")  # Add this line for debugging
            return redirect('dashboard:patient')

        print("Form is not valid")  # Add this line for debugging
        context = {
            'patient': patient,
            'remarks': remarks,
            'form': form,
        }

        return render(request, self.template_name, context)

def index(request):
     # Retrieve counts
    appointment_count = Appointment.objects.count()
    patient_count = Patient.objects.count()
    blog_count = Blog.objects.count()

    context = {
        'appointment_count': appointment_count,
        'patient_count': patient_count,
        'blog_count': blog_count,
    }
    return render(request,'dashboard/index.html',context)

def addblog(request):
    return render(request,'dashboard/addblog.html')

def detail(request):
    return render(request,'dashboard/patient_detail.html')

def appoinments(request):
    appoinments=Appointment.objects.all()
    return render(request,'dashboard/appoinments.html',{'appoinments':appoinments})
class AppointmentEditView(View):
    template_name = 'dashboard/appointmentedit.html'

    def get(self, request, pk):
        appointment = get_object_or_404(Appointment, pk=pk)
        form = AppointmentEditForm(instance=appointment)
        return render(request, self.template_name, {'appointment': appointment, 'form': form})

    def post(self, request, pk):
        appointment = get_object_or_404(Appointment, pk=pk)
        form = AppointmentEditForm(request.POST, instance=appointment)

        if form.is_valid():
            form.save()
            return redirect('dashboard:appointments')  # Correct the redirect URL
        else:
            # Print form errors and data to the console for debugging
            print("Form errors:", form.errors)
            print("Form data:", request.POST)

        return render(request, self.template_name, {'appointment': appointment, 'form': form})
    

class AppointmentDeleteView(View):
    def get(self, request, pk):
        patient = get_object_or_404(Appointment, pk=pk)
        patient.delete()
        return redirect('dashboard:appoinments')    
    
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



def logout_view(request):
    logout(request)
    # Redirect to a specific URL after logout, or to the homepage
    return redirect('dashboard:login')    


