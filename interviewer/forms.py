from django import forms
from .models import Interviewer

class InterviewerForm(forms.ModelForm):
    
    class Meta:
        model = Interviewer
        fields = ['name', 'email', 'phone', 'company_name', 'position']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Full Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email Id'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter Phone Number'}),
            'company_name': forms.TextInput(attrs={'placeholder': 'Enter Company'}),
            'position': forms.TextInput(attrs={'placeholder': 'Enter Position'}),
        }
