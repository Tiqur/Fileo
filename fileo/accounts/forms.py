from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import FileoUser

User = FileoUser()

class UserLoginForm(forms.Form):
    username = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError('This user does not exist')

            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')

            if not user.is_active:
                raise forms.ValidationError('This user is not active')

            return super(UserLoginForm, self).clean(*args, **kwargs)

        
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Add a valid email address')

    class Meta:
        model = FileoUser
        fields = ('email', 'username', 'password1', 'password2')
