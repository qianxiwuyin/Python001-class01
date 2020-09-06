from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=11)
    password = forms.CharField(widget=forms.PasswordInput,min_length=8)