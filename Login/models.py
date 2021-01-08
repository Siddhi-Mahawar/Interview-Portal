from django.db import models
from django.urls import reverse


class CompanyAdmin(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=500)
    phone = models.CharField(max_length=10)
    company_name = models.CharField(max_length=1000)
    username = models.CharField(max_length=250, primary_key=True)
    password = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('Login:Signup', kwargs={'pk': self.pk})
