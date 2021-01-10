from django.http import HttpResponse
from interviewer.forms import InterviewerForm
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
        return redirect('Login:index')

    context['form']= form 
    return render(request, "interviewer/index.html", context)