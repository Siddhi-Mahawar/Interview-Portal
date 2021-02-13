from .models import Interviewer
from Login.models import CompanyAdmin
from editor.models import InterviewRoom
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.utils.timezone import activate
from datetime import datetime
import collections
from django.utils.crypto import get_random_string

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

def getInterviews(email_id):

    interviewer = get_object_or_404(Interviewer, pk = email_id)
    today = timezone.localtime(timezone.now()).replace(hour=0, minute=0, second=0, microsecond=0)
    tomorrow = today + timezone.timedelta(days=1)
    interview_rooms = InterviewRoom.objects.filter(interviewer=interviewer).order_by('startTime')
    
    interviews = collections.defaultdict(list)
    for interview_room in interview_rooms:
        if interview_room.startTime < today:
            interviews['past'].append(interview_room)
        elif interview_room.startTime >= today and interview_room.startTime < tomorrow:
            interviews['today'].append(interview_room)
        else:
            interviews['future'].append(interview_room)
    return interviews