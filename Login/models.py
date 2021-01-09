from django.db import models
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from Login.utilities import ten_minutes_hence

class CompanyAdmin(models.Model):

    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=500, primary_key=True)
    phone = models.CharField(max_length=13)
    company_name = models.CharField(max_length=1000)
    password = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('Login:index')

    def save(self):
        self.password = make_password(self.password)
        super(CompanyAdmin,self).save()



class Verification(models.Model):

    admin_email = models.ForeignKey(CompanyAdmin, on_delete = models.CASCADE)
    token = models.CharField(max_length=200, default="hey")
    timestamp = models.DateTimeField(default=ten_minutes_hence())