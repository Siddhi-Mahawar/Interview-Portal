from django import forms
from Login.models import CompanyAdmin

class CompanyAdminForm(forms.ModelForm):

    password = forms.CharField(max_length=16, widget=forms.PasswordInput)
    
    class Meta:
        model = CompanyAdmin
        fields = ['name', 'email', 'phone', 'company_name', 'password']

class LoginForm(forms.Form):

    email = forms.EmailField(max_length=250)
    password = forms.CharField(max_length=16, widget=forms.PasswordInput)        