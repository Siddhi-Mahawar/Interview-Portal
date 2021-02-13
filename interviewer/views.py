from django.http import HttpResponse
from .forms import InterviewerForm
from .utilities import createInterviewer, createRoom, getInterviews
from django.shortcuts import render, redirect
from editor.forms import InterviewRoomForm
from interviewer.models import Interviewer
from interviewee.models import Interviewee
from editor.models import InterviewRoom
from django.utils.crypto import get_random_string
from datetime import datetime
from django.utils import timezone



def InterviewerCreate(request):
    context = {} 
  
    # create object of form 
    form = InterviewerForm(request.POST or None, request.FILES or None) 
      
    # check if form data is valid 
    if form.is_valid():
        createInterviewer(form, request.session['email'])
        return redirect('Login:home')

    context['form'] = form
    return render(request, "Login/add_interviewer.html", context)

def HomePage(request):
    interview_rooms = getInterviews(request.session['email'])
    return render(request, 'interviewer/homepage.html', {'today_interview': interview_rooms['today'], 'past_interview': interview_rooms['past'], 'future_interview': interview_rooms['future']})


def profile(request):
    interviewer = Interviewer.objects.filter(email=request.session['email'])
    return render(request, 'interviewer/profile.html', {'interviewer': interviewer[0]})


def interviewsScheduled(request):
    interview_rooms = getInterviews(request.session['email'])
    return render(request, 'interviewer/interviewscheduled.html', {'today_interview': interview_rooms['today'], 'past_interview': interview_rooms['past'], 'future_interview': interview_rooms['future']})


def addinterviews(request):
    
    context = {} 
  
    # create object of form 
    form = InterviewRoomForm(request.POST or None, request.FILES or None) 
      
    # check if form data is valid 
    if form.is_valid(): 
        token = get_random_string(length=32)
        createRoom(form, request.session['email'], token)  
        return redirect('interviewer:home')


    context['form']= form 
    return render(request, 'interviewer/addinterviews.html', context)


def gotoeditor(request, roomId):
    return redirect('editor:editor', roomId=roomId)

