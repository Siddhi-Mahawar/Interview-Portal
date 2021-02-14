from django import forms
from Login.models import CompanyAdmin
from .choices import TYPE_CHOICES


class CompanyAdminForm(forms.ModelForm):

    name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': 'Enter Your Name'}))
    email = forms.EmailField(max_length = 250, widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email Id'}))
    phone = forms.CharField(max_length=13, widget=forms.TextInput(attrs={'placeholder': 'Enter Your Phone Number'}))
    company_name = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'placeholder': 'Enter Your Company Name'}))
    password = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your Password'}))

    class Meta:
        model = CompanyAdmin
        fields = ['name', 'email', 'phone', 'company_name', 'password']


class LoginForm(forms.Form):

    email = forms.EmailField(max_length = 250, widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'placeholder': 'Password'})) 
    user_type = forms.ChoiceField(choices=TYPE_CHOICES)


class VerificationForm(forms.Form):

    email = forms.EmailField(max_length=250)

    def __init__(self, email_id, *args, **kwargs):
        super(VerificationForm, self).__init__(*args, **kwargs)
        self.fields['email'] = forms.EmailField(initial=email_id)

class PasswordResetRequestForm(forms.Form):

    email = forms.EmailField(max_length=250, widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email Id'}))

class PasswordResetForm(forms.Form):

    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'placeholder': 'Enter New Password'})) 
    confirm_password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'placeholder': 'Enter New Password Again'})) 