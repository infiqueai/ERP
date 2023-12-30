from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from .models import *

def register(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']

        if password == password2:
            # Create a user using Django's built-in User model
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            user.is_staff = True  # Grant admin panel access
            user.save()
            messages.success(request, 'Registration successful. You can now login.')
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or home page
            return redirect('index')  # Replace 'index' with the URL name of your home page
        else:
            # Display an error message or handle invalid login
            # For example, you can use Django messages framework to show a message
            messages.error(request, 'Invalid login credentials')

    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

from .models import AccountDetails
def accounts(request):
    # Fetch data from the database using your model
    account_data = AccountDetails.objects.all()
    print(account_data)  # Add this line to print the data in the console

    # Pass the data to the template
    return render(request, 'accounts.html', {'account_data': account_data})


def Graphical(request):
    return render(request, 'graphical.html')


from .forms import CommonStudentForm, Table1Form, Table2Form
from .models import Table1, Table2

def groupby(request):
    if request.method == 'POST':
        session = request.POST.get('session')

        if session == '2021-2022':
            data = Table1.objects.all()
        elif session == '2020-2021':
            data = Table2.objects.all()
        else:
            data = CommonStudent.objects.all()

        return render(request, 'groupby.html', {'data': data, 'session': session})
    
    return render(request, 'groupby.html')

def student_form(request):
    return render(request, 'student_form.html')

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

def studentdetails(request):
    student_data = StudentDetails.objects.all()

    # Number of records to display per page
    records_per_page = int(request.GET.get('page_size', 80))  # Default to 80 if not provided

    paginator = Paginator(student_data, records_per_page)
    page = request.GET.get('page')

    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page.
        results = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page of results.
        results = paginator.page(paginator.num_pages)

    return render(request, 'student_details.html', {'results': results})


def staffdetails(request):
    return render(request, 'staff_details.html')

def Staff(request):
    return render(request, 'staff.html')

def Student(request):
    return render(request, 'student.html')

def receipt(request):
    return render(request, 'receipt.html')

def penalty(request):
    return render(request, 'penalty.html')

def important_notice(request):
    return render(request, 'important_notice.html')

def certificate(request):
    return render(request, 'certificate.html')

def complaint(request):
    return render(request, 'complaint.html')

def Logout(request):
    logout(request)
    return redirect('login')

def dashboard(request):
   return render(request, 'dashboard.html')  

def sports(request):
   return render(request, 'sports.html')  

def setpaper(request):
   return render(request, 'setpaper.html')  

def holidays(request):
   return render(request, 'holidays.html')  

def bus(request):
   return render(request, 'bus.html')  

def smsservices(request):
   return render(request, 'smsservices.html') 

def timetable(request):
   return render(request, 'timetable.html') 

def weekly(request):
   return render(request, 'weekly.html') 

def gallery(request):
   return render(request, 'gallery.html') 

def dues(request):
   return render(request, 'dues.html') 

def result(request):
   return render(request, 'result.html') 

def government(request):
   return render(request, 'government.html') 

def hostel(request):
   return render(request, 'hostel.html') 

def session(request):
   return render(request, 'session.html')

def session(request):
   return render(request, 'session1.html')

def hostel_A(request):
   return render(request, 'hostel_A.html') 

def hostel_B(request):
   return render(request, 'hostel_B.html') 

def hostel_C(request):
   return render(request, 'hostel_C.html') 


def homework(request):
   return render(request, 'homework.html') 


def download(request):
   return render(request, 'download.html') 

def library(request):
   return render(request, 'library.html') 

def events(request):
   return render(request, 'events.html') 


def examination(request):
   return render(request, 'examination.html') 

def leave(request):
   return render(request, 'leave.html')  

def client(request):
   return render(request, 'client.html')  

def home(request):
   return render(request, 'home.html') 

def deal(request):
   return render(request, 'deals.html') 


def activityreport(request):
   return render(request, 'activityreport.html') 

def salesperformance(request):
   return render(request, 'salesperformance.html') 

def salestarget(request):
   return render(request, 'salestarget.html') 

from .forms import StdInsertForm
def Insertrecord(request):
    if request.method == 'POST':
        form = StdInsertForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record saved successfully..!')
            return redirect('index')  # Redirect to a success page
        else:
            messages.error(request, 'Record could not be saved.')
    
    else:
        form = StdInsertForm()

    return render(request, 'student_form.html', {'form': form})


from .forms import ReceiptForm
def submit_receipt(request):
    if request.method == 'POST':
        form = ReceiptForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record saved successfully..!')
            return redirect('index')  # Redirect to a success page
        else:
            messages.error(request, 'Record could not be saved.')
    
    else:
        form = ReceiptForm()

    return render(request, 'receipt.html', {'form': form})

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Table1, Table2  

@require_POST
def search_data(request):
    session = request.POST.get('session')
    selected_class = request.POST.get('class')
    name = request.POST.get('name')
    admission_number = request.POST.get('admissionNumber')
    father_name = request.POST.get('fatherName')
    father_mobile_number = request.POST.get('fatherMobileNumber')

    search_results_table1 = Table1.objects.filter(
        startyear=session,
        ClassSequenceNumber=selected_class,
        Name__icontains=name,
        AdmissionNumber__icontains=admission_number,
        FatherName__icontains=father_name,
        FatherMobile__icontains=father_mobile_number
    ).values()

    search_results_table2 = Table2.objects.filter(
        startyear=session,
        ClassSequenceNumber=selected_class,
        Name__icontains=name,
        AdmissionNumber__icontains=admission_number,
        FatherName__icontains=father_name,
        FatherMobile__icontains=father_mobile_number
    ).values()

    
    search_results = list(search_results_table1) + list(search_results_table2)

    return JsonResponse(search_results, safe=False)














