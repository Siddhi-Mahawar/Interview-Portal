from django.shortcuts import render, get_object_or_404
from .models import CompanyAdmin, Verification, Passwordrequest
from interviewer.models import Interviewer
from interviewee.models import Interviewee
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import Http404
from Login.forms import CompanyAdminForm, LoginForm, VerificationForm, PasswordResetForm, PasswordResetRequestForm
from Login.helper import send_activation_email, checkTimestamp, ten_minutes_hence, send_reset_email
from Login.utilities import admin_Login, interviewer_Login, interviewee_Login
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import make_password


def LoginView(request):

    if 'email' in request.session:
        return redirect('Login:home')

    context = {} 
    
    # create object of form 
    form = LoginForm(request.POST or None, request.FILES or None) 
      
    # check if form data is valid 
    if form.is_valid(): 
        
        if form.cleaned_data['user_type'] == "1":
            print (form.cleaned_data)
            user = admin_Login(form)
            if user.pk:
                request.session['email'] = user.email
                request.session['valid'] = user.is_active
                request.session['user_type'] = "Admin"
                return redirect('Login:home')

        elif form.cleaned_data['user_type'] == "2":
            
            user = interviewer_Login(form)
            if user.pk:
                request.session['email'] = user.email
                request.session['user_type'] = "Interviewer"
                return redirect('interviewer:home')
        
        else:
            
            user = interviewee_Login(form)
            if user.pk:
                request.session['email'] = user.email
                request.session['interviewee_pk'] = user.pk
                request.session['valid'] = user.is_active
                request.session['user_type'] = "Interviewee"
                return redirect('interviewee:home')
        
    context['form']= form 
    return render(request, "Login/login.html", context) 

def HomePage(request):

    print (request.session['user_type'])
    if 'user_type' in request.session:
        if request.session['user_type'] == "Interviewer":
            return redirect('interviewer:home')
        elif request.session['user_type'] == "Interviewee":
            return redirect('interviewee:home')
        else:
            if request.session['valid'] is False:
                return redirect('Login:admin-email-verification') 
            else:
                admin = CompanyAdmin.objects.get(email=request.session['email'])
                print(admin)
                return render(request, "Login/profile.html", {'admin' : admin }) 
    else:
        return redirect('Login:login')



def AdminCreate(request):

    if 'email' in request.session:
        return redirect('Login:home')

    context = {} 
  
    # create object of form 
    form = CompanyAdminForm(request.POST or None, request.FILES or None) 
      
    # check if form data is valid 
    if form.is_valid(): 
        form.save() 
        return redirect('Login:login')

    context['form'] = form
    return render(request, "Login/signup.html", context) 


def AdminEmailVerification(request):

    if not 'email' in request.session:
        return redirect('Login:login')

    if request.session['valid']:
        return redirect('Login:home')

    admin_email_id = request.session['email']

    if request.method == "GET":

        context = {} 
        form = VerificationForm(email_id=admin_email_id)

        context['form'] = form
        return render(request, "Login/verification_form.html", context)
    
    if request.method == "POST":

        token = get_random_string(length=32)
        to_email_id_list = admin_email_id
        send_activation_email(to_email_id_list, token)

        admin = get_object_or_404(CompanyAdmin, pk = admin_email_id)
        
        try:
            verify_row = Verification.objects.get(admin_email = admin)
        except Verification.DoesNotExist:
            print('sending stuff')
            verify_row = Verification()
            verify_row.admin_email = admin
        verify_row.token = token
        verify_row.timestamp = ten_minutes_hence()
        verify_row.save()

        return redirect('Login:admin-email-verification')


def EmailVerify(request, token_value):

    verify_object = Verification.objects.get(token= token_value)
    
    if checkTimestamp(verify_object.timestamp):
        admin = verify_object.admin_email
        admin.is_active = True
        admin.save()

        request.session['email'] = admin.email
        request.session['valid'] = admin.is_active

    return redirect('Login:login')

def ResetPasswordRequest(request):

    context = {}

    # create object of form
    form = PasswordResetRequestForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():

            token = get_random_string(length=32)
            to_email_id = form.cleaned_data['email']
            send_reset_email(to_email_id, token)

            admin = get_object_or_404(CompanyAdmin, pk=to_email_id)
            
            try:
                passwordresetrow = Passwordrequest.objects.get(admin_email=admin)
            except Passwordrequest.DoesNotExist:
                passwordresetrow = Passwordrequest()
                passwordresetrow.admin_email = admin
            
            passwordresetrow.token = token
            passwordresetrow.timestamp = ten_minutes_hence()
            passwordresetrow.save()
            return redirect('Login:login')

    context['form'] = form
    return render(request, "Login/forgot_password.html", context)

def ResetPassword(request, token_value):

    context = {} 
  
    # create object of form 
    form = PasswordResetForm(request.POST or None, request.FILES or None) 
      
    # check if form data is valid 
    if form.is_valid(): 
        
        print (form.cleaned_data)
        if form.cleaned_data['password'] == form.cleaned_data['confirm_password']:
            try:
                reset_password_object = Passwordrequest.objects.get(token= token_value)
                if checkTimestamp(reset_password_object.timestamp):
                    admin = reset_password_object.admin_email
                    admin.password = form.cleaned_data['password']
                    admin.save()
                    return redirect('Login:login')
            except Passwordrequest.DoesNotExist:
                return redirect('Login:login')

    context['form'] = form
    return render(request, "Login/update_password.html", context) 


def Logout(request):
    
    try:
        del request.session['email']
        del request.session['user_type']
        del request.session['valid']
        del request.session['interviewee_pk']
    except KeyError:
        pass

    return redirect('Login:login')



def Interviewers(request):

    if 'email' in request.session:
        interviewers = Interviewer.objects.filter(admin_email=request.session['email'])
        print (interviewers)
        return render(request, "Login/interviewers.html", {'interviewers' : interviewers}) 
    else:
        return redirect('Login:login')


def Interviewees(request):

    if 'email' in request.session:
        interviewees = Interviewee.objects.filter(admin_email=request.session['email'])
        return render(request, "Login/interviewees.html", {'interviewees' : interviewees}) 
    else:
        return redirect('Login:login')