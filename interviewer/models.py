from django.db import models
from Login.models import CompanyAdmin

# Create your models here.
class Interviewer(models.Model):

    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=500, primary_key=True)
    phone = models.CharField(max_length=13)
    company_name = models.CharField(max_length=1000)
    position = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    admin_email = models.ForeignKey(CompanyAdmin, on_delete = models.CASCADE)