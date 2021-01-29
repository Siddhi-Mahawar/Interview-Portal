from .models import Interviewer
from Login.models import CompanyAdmin
from editor.models import InterviewRoom
from django.shortcuts import get_object_or_404

def createInterviewer(form, admin_email_id):
    
    cleaned_data = form.cleaned_data
    admin = get_object_or_404(CompanyAdmin, pk = admin_email_id)

    interviewer = Interviewer()
    interviewer.name = cleaned_data['name']
    interviewer.email = cleaned_data['email']
    interviewer.phone = cleaned_data['phone']
    interviewer.company_name = cleaned_data['company_name']
    interviewer.position = cleaned_data['position']
    interviewer.password = get_random_string(length=32)
    interviewer.admin_email = admin
    interviewer.save()

def createRoom(form, admin_email_id, token):
    
    cleaned_data = form.cleaned_data
    interviewer = get_object_or_404(Interviewer, pk = admin_email_id)

    room = InterviewRoom()
    room.startTime = cleaned_data['startTime']
    room.endTime = cleaned_data['endTime']
    room.question = cleaned_data['question']
    room.token = token
    room.interviewee = cleaned_data['interviewee']
    room.interviewer = interviewer
    room.save()
