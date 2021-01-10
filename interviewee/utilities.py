from .models import Interviewee
from Login.models import CompanyAdmin
from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string

def createInterviewee(form, admin_email_id):
    
    cleaned_data = form.cleaned_data
    admin = get_object_or_404(CompanyAdmin, pk = admin_email_id)

    interviewee = Interviewee()
    interviewee.email = cleaned_data['email']
    interviewee.password = get_random_string(length=30)
    interviewee.timestamp = cleaned_data['timestamp']
    interviewee.admin_email = admin

    interviewee.save()

    print (cleaned_data)