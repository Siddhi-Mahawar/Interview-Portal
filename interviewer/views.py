from django.http import HttpResponse
from .forms import InterviewerForm
from .utilities import createInterviewer, createRoom
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
    return render(request, "interviewer/index.html", context)

def HomePage(request):
    #return HttpResponse("This is home page")
    # if request.session['valid'] is False:
    #     return redirect('interviewer:details')
    # else:
    print (request.session['email'])
    today = timezone.now()
    tomorrow = timezone.now()+timezone.timedelta(days=1)
    print(tomorrow)
    interviewee = Interviewee.objects.all()
    interviewer = Interviewer.objects.filter(email=request.session['email'])
    interview = InterviewRoom.objects.filter(interviewer=interviewer[0]).order_by('startTime')
    print(interviewee[0])
    print(interview)
    print(datetime.now().date())
    return render(request, 'interviewer/homepage.html', {'interviewees': interviewee, 'interview': interview, 'interviewer': interviewer[0],'today':today, 'tomorrow':tomorrow})


def profile(request):
    return render(request, 'interviewer/profile.html')


def interviewsScheduled(request):
    return render(request, 'interviewer/interviewsscheduled.html')


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

