from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import IntervieweeForm
from .utilities import createInterviewee

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
    return render(request, "interviewer/index.html", context)

def HomePage(request):
    return HttpResponse("This is home page")