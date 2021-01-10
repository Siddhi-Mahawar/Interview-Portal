from django import forms
from interviewer.models import Interviewer

class InterviewerForm(forms.ModelForm):
    
    class Meta:
        model = Interviewer
        fields = ['name', 'email', 'phone', 'company_name', 'position']
