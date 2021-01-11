from django import forms
from Login.models import CompanyAdmin
from .choices import TYPE_CHOICES


class CompanyAdminForm(forms.ModelForm):

    password = forms.CharField(max_length=16, widget=forms.PasswordInput)
    
    class Meta:
        model = CompanyAdmin
        fields = ['name', 'email', 'phone', 'company_name', 'password']


class LoginForm(forms.Form):

    email = forms.EmailField(max_length=250)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput) 
    user_type = forms.ChoiceField(choices=TYPE_CHOICES)


class VerificationForm(forms.Form):

    email = forms.EmailField(max_length=250)

    def __init__(self, email_id, *args, **kwargs):
        super(VerificationForm, self).__init__(*args, **kwargs)
        self.fields['email'] = forms.EmailField(initial=email_id)


class PasswordResetForm(forms.Form):
    password1 = forms.CharField(label='New password', widget=forms.PasswordInput, max_length=16)
    password2 = forms.CharField(label='New password (confirm)', widget=forms.PasswordInput, max_length=16)

    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
        self.fields['password1'] = forms.PasswordInput()
        self.fields['password2'] = forms.PasswordInput()
