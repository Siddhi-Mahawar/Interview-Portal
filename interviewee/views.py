from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import IntervieweeForm, IntervieweeDetailsForm
from .utilities import createInterviewee, UpdateIntervieweeDetails, getInterviews
from interviewer.models import Interviewer
from interviewee.models import Interviewee
from editor.models import InterviewRoom
import json

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

def Profile(request):

    if 'email' in request.session:
        if request.session['valid'] is False:
            return redirect('interviewee:details') 
        else:
            interviewee = Interviewee.objects.get(pk = request.session['interviewee_pk'])
            return render(request, 'interviewee/profile.html', {'interviewee': interviewee })
    return redirect('Login:login')

def interviewsScheduled(request):
    interviews = getInterviews(request.session['interviewee_pk'])['today']
    print (interviews)
    return render(request, 'interviewee/interviewsScheduled.html',{'interviews': interviews})

def IntervieweeDetails(request):
    
    if request.session['valid']:
        return redirect('interviewee:home')

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