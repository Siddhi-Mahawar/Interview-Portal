from django.db import models
from interviewee.models import Interviewee
from interviewer.models import Interviewer

# Create your models here.
class InterviewRoom(models.Model):

    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    token = models.CharField(max_length=32, default="hey")
    interviewer = models.ForeignKey(Interviewer, on_delete=models.CASCADE)
    interviewee = models.ForeignKey(Interviewee, on_delete=models.CASCADE)
    question = models.TextField()
    freeze = models.BooleanField(default=False)
    lang = models.CharField(max_length=50, default='text/x-c++src')
