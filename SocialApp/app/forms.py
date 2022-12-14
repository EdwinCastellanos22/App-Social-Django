from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email= forms.EmailField(required=True)
    password1= forms.CharField(required=True, label='Insert Password', widget=forms.PasswordInput)
    password2= forms.CharField(required=True, label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model= User
        fields= ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user