from django.db import models
from Login.models import CompanyAdmin

# Create your models here.
class Interviewee(models.Model):

    name = models.CharField(max_length=250, default="")
    email = models.EmailField(max_length=500)
    phone = models.CharField(max_length=13, default="")
    password = models.CharField(max_length=100)
    resume_link = models.CharField(max_length = 1000, default="")
    timestamp = models.DateTimeField()
    admin_email = models.ForeignKey(CompanyAdmin, on_delete = models.CASCADE)
    is_active = models.BooleanField(default=False)