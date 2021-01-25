from Login.models import CompanyAdmin
from interviewer.models import Interviewer
from interviewee.models import Interviewee
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import check_password
from django.utils import timezone

def admin_Login(form):
    
    user_email = form.cleaned_data['email']
    user_password = form.cleaned_data['password']

    try:
        user = CompanyAdmin.objects.get(email = user_email)
        if check_password(user_password, user.password):        
            return user
    
        return CompanyAdmin()

    except CompanyAdmin.DoesNotExist:
        return CompanyAdmin()


def interviewer_Login(form):
    
    user_email = form.cleaned_data['email']
    user_password = form.cleaned_data['password']

    print (user_email, user_password)

    try:
        user = Interviewer.objects.get(email = user_email, password = user_password)
        return user

    except Interviewer.DoesNotExist:
        return Interviewer()


def interviewee_Login(form):
    
    user_email = form.cleaned_data['email']
    user_password = form.cleaned_data['password']

    try:
        user = Interviewee.objects.get(email = user_email, password = user_password)
        if user.timestamp > timezone.now():
            return user

    except Interviewee.DoesNotExist:
        return Interviewee()

    return Interviewee()
