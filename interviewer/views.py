from django.http import HttpResponse
from .forms import InterviewerForm
from .utilities import createInterviewer
from django.shortcuts import render, redirect

# Create your views here.
def InterviewerCreate(request):
    context = {} 
  
    # create object of form 
    form = InterviewerForm(request.POST or None, request.FILES or None) 
      
    # check if form data is valid 
    if form.is_valid():
        createInterviewer(form, request.session['email'])
        return redirect('Login:home')

    context['form']= form 
    return render(request, "interviewer/index.html", context)

def HomePage(request):
    #return HttpResponse("This is home page")
    return render(request, 'interviewer/homepage.html')


def profile(request):
    return render(request, 'interviewer/profile.html')


def interviewsScheduled(request):
    return render(request, 'interviewer/interviewsscheduled.html')


def addinterviews(request):
    return render(request, 'interviewer/addinterviews.html')