from django import forms
from .models import Interviewee
from project import settings

class IntervieweeForm(forms.ModelForm):
    
    timestamp = forms.DateTimeField(input_formats=['%Y-%m-%d'])

    class Meta:
        model = Interviewee
        fields = ['email', 'timestamp']

class IntervieweeDetailsForm(forms.ModelForm):

    class Meta:
        model = Interviewee
        fields = ['name', 'phone', 'resume_link']