from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User

from usermanagement.models import CustomUser
from . import forms


def index(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method== 'POST':
        form = forms.Login(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                print("error data")
                return render(request,'login.html',{'err':'incorrect data'})
        else:
            return render(request,'login.html',{'err':'add valid details'})
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        user_form = forms.UserRegistrationForm(request.POST)
        print("ok clean user form")
        if user_form.is_valid():
            print("valid field")
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()
            login(request,new_user)
            return redirect('home')
        else:
            print("user form is not valid",user_form.errors)
            return render(request,'register.html',{'error':user_form.errors})

    return render(request,'register.html')

@login_required
def home(request):
    return render(request,'index.html')

@login_required
def review(request):
    return render(request,'review.html')

@login_required
def logout_out(request):
    logout(request)
    return redirect('index')

