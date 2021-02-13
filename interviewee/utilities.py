from .models import Interviewee
from Login.models import CompanyAdmin
from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string
from django.utils import timezone
from editor.models import InterviewRoom
import collections

def createInterviewee(form, admin_email_id):
    
    cleaned_data = form.cleaned_data
    admin = get_object_or_404(CompanyAdmin, pk = admin_email_id)

    interviewee = Interviewee()
    interviewee.email = cleaned_data['email']
    interviewee.password = get_random_string(length=30)
    interviewee.timestamp = cleaned_data['timestamp']
    interviewee.admin_email = admin

    interviewee.save()

def UpdateIntervieweeDetails(form, interviewee_pk):

    cleaned_data = form.cleaned_data
    interviewee = get_object_or_404(Interviewee, pk = interviewee_pk)

    interviewee.name = cleaned_data['name']
    interviewee.phone = cleaned_data['phone']
    interviewee.resume_link = cleaned_data['resume_link']
    interviewee.is_active = True

    interviewee.save()

def getInterviews(key):

    interviewee = get_object_or_404(Interviewee, pk = key)
    today = timezone.localtime(timezone.now()).replace(hour=0, minute=0, second=0, microsecond=0)
    tomorrow = today + timezone.timedelta(days=1)

    interview_rooms = InterviewRoom.objects.filter(interviewee=interviewee).order_by('startTime')    
    interviews = collections.defaultdict(list)

    for interview_room in interview_rooms:
        if interview_room.startTime < today:
            interviews['past'].append(interview_room)
        elif interview_room.startTime >= today and interview_room.startTime < tomorrow:
            interviews['today'].append(interview_room)
        else:
            interviews['future'].append(interview_room)
    return interviews
