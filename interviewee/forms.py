from django import forms
from .models import Interviewee
from project import settings

class IntervieweeForm(forms.ModelForm):
    
    timestamp = forms.DateTimeField(input_formats=['%Y-%m-%d'])

    class Meta:
        model = Interviewee
        fields = ['email', 'timestamp']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'timestamp': forms.DateTimeInput(attrs={'placeholder': 'TimeStamp'}),
        }

class IntervieweeDetailsForm(forms.ModelForm):

    class Meta:
        model = Interviewee
        fields = ['name', 'phone', 'resume_link']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Full Name'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter Phone Number'}),
            'resume_link': forms.TextInput(attrs={'placeholder': 'Enter Resume Link'}),
        }