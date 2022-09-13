from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login
from .models import *
 
 
# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_patient:
                login(request, user)
                return redirect('patient')
            elif user is not None and user.is_doctor:
                login(request, user)
                return redirect('doctor')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def admin(request):
    return render(request,'admin.html')


def patient(request):
    return render(request,'patient.html')


def doctor(request):
    return render(request,'doctor.html')

def create_blog(request):
    doctors = User.objects.all().filter(is_doctor=True)
    print(doctors)
    print(request.user)
    print(request)
    if request.user in doctors:
        print("test")
        print(request.method)
        if request.method == "POST":
            form = Blog_form(request.POST)
            if form.is_valid():
                print("before save")
                form.save()
                print("after save")

            return render(request, 'createblog.html', {"form":form})
        else:
            form = Blog_form()
            return render(request, 'createblog.html', {"form":form})
    else:
        print("no doctor")
        return HttpResponse("<h1>no doctor</h1>")

def show_blogs(request):
    blogs = Blog.objects.all().filter(draft = False)
    print(blogs)
    return render(request,'showblogs.html',{'blogs':blogs})
    

# def update(request,id):
#     doctors = User.objects.all().filter(is_doctor=True)
#     blog = Blog.objects.all().filter(id = id)
#     print(doctors)
#     print(request.user)
#     print(request)
#     if request.user in doctors:
#         print("test")
#         print(request.method)
#         if request.method == "POST":
#             form = Blog_form(request.POST, instance=blog)
#             if form.is_valid():
#                 print("before save")
#                 form.save()
#                 print("after save")
#                 return render(request,'updateblogs.html',{'form':form})
#         else:

#             form = Blog_form(instance=blog)
#             return render(request,'updateblogs.html',{'form':form})

def book_app(request):
    return render(request,'bookapp.html')

def details_appointment(request):
    return render(request, 'details_app.html')
