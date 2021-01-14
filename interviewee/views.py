from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import IntervieweeForm, IntervieweeDetailsForm
from .utilities import createInterviewee, UpdateIntervieweeDetails

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
    return render(request, "interviewee/index.html", context)

def HomePage(request):

    if request.session['valid'] is False:
        return redirect('interviewee:details')

    print (request.session['email'])
    # return HttpResponse("This is home page of interviewee")
    return render(request, 'interviewee/homepage.html')


def profile(request):
    return render(request, 'interviewee/profile.html')


def interviewsScheduled(request):
    return render(request, 'interviewee/interviewsscheduled.html')


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