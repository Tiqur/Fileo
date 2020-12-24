from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import FileoUser

User = FileoUser()

class UserLoginForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = FileoUser
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Invalid login')
        

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Add a valid email address')

    class Meta:
        model = FileoUser
        fields = ('email', 'username', 'password1', 'password2')
