from django import forms
from .models import Interviewee
from project import settings

class IntervieweeForm(forms.ModelForm):
    
    timestamp = forms.DateTimeField(input_formats=['%Y-%m-%d'])

    class Meta:
        model = Interviewee
        fields = ['email', 'timestamp']
