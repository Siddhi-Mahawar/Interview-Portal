from django.shortcuts import render
from .models import CompanyAdmin
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.http import Http404


def index(request):
    return render(request, 'Login/index.html')


def detail(request):
    return render(request, 'Login/detail.html')


class IndexView(generic.ListView):
    template_name = 'Login/index.html'

    def get_queryset(self):
        return CompanyAdmin.objects.all()


class DetailView(generic.DetailView):
    model = CompanyAdmin
    template_name = 'Login/detail.html'


class AdminCreate(CreateView):
    model = CompanyAdmin
    fields = ['name', 'email', 'phone', 'company_name', 'username', 'password']


class AdminDelete(DeleteView):
    model = CompanyAdmin
    success_url = reverse_lazy('Login:index')

