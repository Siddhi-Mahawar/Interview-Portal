from django.shortcuts import render
from .models import CompanyAdmin
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.http import Http404
from Login.forms import CompanyAdminForm, LoginForm
from django.contrib.auth.hashers import make_password, check_password

def LoginView(request):

    if 'email' in request.session:
        return redirect('Login:home')

    context = {} 
    
    # create object of form 
    form = LoginForm(request.POST or None, request.FILES or None) 
      
    # check if form data is valid 
    if form.is_valid(): 
        
        user_email = form.cleaned_data['email']
        user_password = form.cleaned_data['password']
        user = CompanyAdmin.objects.get(email = user_email)
        
        if check_password(user_password, user.password):
            request.session['email'] = user.email
            return redirect('Login:home')

    context['form']= form 
    return render(request, "Login/index.html", context) 

def HomePage(request):

    if 'email' in request.session:
        return render(request, "Login/detail.html") 
    else:
        return redirect('Login:index')

def AdminCreate(request):

    if 'email' in request.session:
        return redirect('Login:home')

    context = {} 
  
    # create object of form 
    form = CompanyAdminForm(request.POST or None, request.FILES or None) 
      
    # check if form data is valid 
    if form.is_valid(): 
        form.save() 
        return redirect('Login:index')

    context['form']= form 
    return render(request, "Login/companyadmin_form.html", context) 
