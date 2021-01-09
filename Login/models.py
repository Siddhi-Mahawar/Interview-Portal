from django.db import models
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from django.contrib.auth.hashers import make_password

class CompanyAdmin(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=500)
    phone = models.CharField(max_length=13)
    company_name = models.CharField(max_length=1000)
    username = models.CharField(max_length=250, primary_key=True)
    password = models.CharField(max_length=16)

    def get_absolute_url(self):
        return reverse('Login:index')

    def save(self):
        self.password = make_password(self.password)
        super(CompanyAdmin,self).save()
