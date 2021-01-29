from django import forms
from .models import InterviewRoom


class InterviewRoomForm(forms.ModelForm):
    
    startTime = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M:%S'])
    endTime = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M:%S'])
    interviewee = forms.TextInput()
    
    class Meta:
        model = InterviewRoom
        fields = ['startTime', 'endTime', 'question', 'interviewee']
        widgets = {
            'startTime': forms.DateTimeInput(attrs={'placeholder': 'Start TimeStamp'}),
            'endTime': forms.DateTimeInput(attrs={'placeholder': 'End TimeStamp'}),
            'question': forms.Textarea(attrs={'placeholder': 'Enter Question'}),
            'interviewee': forms.TextInput(attrs={'placeholder': 'Enter Interviewee Id'}),
        }
