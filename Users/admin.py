from django.contrib import admin
from .models import Interviewee, Interviewer
# Register your models here.

admin.site.register(Interviewer)
admin.site.register(Interviewee)