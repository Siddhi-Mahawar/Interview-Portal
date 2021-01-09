from django.shortcuts import render
from .models import CompanyAdmin
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.http import Http404
from Login.forms import CompanyAdminForm
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string


class IndexView(generic.ListView):
    template_name = 'Login/index.html'

    def get_queryset(self):
        return CompanyAdmin.objects.all()


class DetailView(generic.DetailView):
    model = CompanyAdmin
    template_name = 'Login/detail.html'


def AdminCreate(request):
    context = {}

    form = CompanyAdminForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        # send_mail(subject, message, from_list, to_list, fail_silently=True)
        token = get_random_string(length=32)
        subject = "Activation mail"
        message = token
        from_list = settings.EMAIL_HOST_USER
        to_list = [save_it.email, settings.EMAIL_HOST_USER]
        send_mail(subject, message, from_list, to_list, fail_silently=True)
        return redirect('Login:index')

    context['form'] = form
    return render(request, 'Login/companyadmin_form.html', context)