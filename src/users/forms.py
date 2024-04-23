from django import forms
from .models import User


class UserSignUpForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("email", "password")


class UserLoginForm(forms.Form):
    email = forms.CharField(max_length=255, label=u'Email')
    password = forms.CharField(max_length=255, widget=forms.PasswordInput, label=u'Password')

