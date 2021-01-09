from django.shortcuts import render
from .models import CompanyAdmin
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.http import Http404
from Login.forms import CompanyAdminForm

class IndexView(generic.ListView):
    template_name = 'Login/index.html'

    def get_queryset(self):
        return CompanyAdmin.objects.all()


class DetailView(generic.DetailView):
    model = CompanyAdmin
    template_name = 'Login/detail.html'

def AdminCreate(request):

    context ={} 
  
    # create object of form 
    form = CompanyAdminForm(request.POST or None, request.FILES or None) 
      
    # check if form data is valid 
    if form.is_valid(): 
        form.save() 
        return redirect('Login:index')

    context['form']= form 
    return render(request, "Login/companyadmin_form.html", context) 
