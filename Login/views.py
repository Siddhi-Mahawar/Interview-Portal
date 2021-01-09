from django.shortcuts import render, get_object_or_404
from .models import CompanyAdmin, Verification
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View, CreateView
from django.http import Http404
from Login.forms import CompanyAdminForm, LoginForm, VerificationForm
from django.contrib.auth.hashers import make_password, check_password
from Login.utilities import send_activation_email
from django.utils.crypto import get_random_string

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

def AdminEmailVerification(request):
    
    admin_email_id = request.session['email']

    if request.method == "GET" :

        context = {} 
        form = VerificationForm(email_id = admin_email_id) 

        context['form']= form 
        return render(request, "Login/verification_form.html", context) 
    
    if request.method == "POST":

        token = get_random_string(length=32)
        to_email_id_list = admin_email_id
        send_activation_email(to_email_id_list, token)

        admin = get_object_or_404(CompanyAdmin, pk = admin_email_id)
        verify_row = Verification(admin_email = admin, token = token)
        verify_row.save()

        return redirect('Login:admin-email-verification')