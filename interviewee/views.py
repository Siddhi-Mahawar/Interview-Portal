from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import IntervieweeForm, IntervieweeDetailsForm
from .utilities import createInterviewee, UpdateIntervieweeDetails
from interviewer.models import Interviewer
from interviewee.models import Interviewee
from editor.models import InterviewRoom
import json

# Create your views here.
def IntervieweeCreate(request):
    context = {} 
  
    # create object of form 
    form = IntervieweeForm(request.POST or None, request.FILES or None) 
      
    # check if form data is valid 
    if form.is_valid():
        print (form.cleaned_data)
        createInterviewee(form, request.session['email'])
        return redirect('Login:home')

    context['form']= form 
    return render(request, "Login/add_interviewee.html", context)

def HomePage(request):

    #if request.session['valid'] is False:
    #    return redirect('interviewee:details')
    #else:
        print (request.session['email'])

        interviewer = Interviewer.objects.all()
        interviewee = Interviewee.objects.filter(email=request.session['email'])
        interview = InterviewRoom.objects.filter(interviewee=interviewee[0])
        print(interviewee[0].email)

        return render(request, 'interviewee/homepage.html', {'interviewers': interviewer, 'interview': interview, 'interviewee':interviewee[0] })

    # return HttpResponse("This is home page of interviewee")



def profile(request):
    interviewee = Interviewee.objects.filter(email=request.session['email'])
    return render(request, 'interviewee/profile.html',{ 'interviewee':interviewee[0] })


def interviewsScheduled(request):
    interviewer = Interviewer.objects.all()
    interviewee = Interviewee.objects.filter(email=request.session['email'])
    interview = InterviewRoom.objects.filter(interviewee=interviewee[0])
    print(interviewee[0].email)
    return render(request, 'interviewee/interviewsScheduled.html',{'interviewers': interviewer, 'interview': interview, 'interviewee':interviewee[0] })


def interviewRequests(request):
    return render(request, 'interviewee/interviewrequests.html')

# Create your views here.
def IntervieweeDetails(request):
    
    if request.session['valid']:
        return redirect('interviewee:home')

    print (request.session['email'])
    print (request.session['user_type'])    
    print (request.session['valid'])

    context = {} 
  
    # create object of form 
    form = IntervieweeDetailsForm(request.POST or None, request.FILES or None) 
      
    # check if form data is valid 
    if form.is_valid():
        
        UpdateIntervieweeDetails(form, request.session['interviewee_pk'])
        request.session['valid'] = True
        return redirect('interviewee:home')

    context['form']= form 
    return render(request, "interviewee/details.html", context)


def gotoeditor(request, roomId):
    return redirect('editor:editor', roomId=roomId)
