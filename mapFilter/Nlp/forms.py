from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *
from Nlp.admin import MyUserCreationForm


class RegisterUserForm(MyUserCreationForm):
    username = forms.CharField(label='Логін', widget=forms.TextInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(label="Ім'я", widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Прізвище', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    confirm_password = forms.CharField(label='Пароль2',
                                       widget=forms.PasswordInput(attrs={'class': 'form-input'}, render_value=False))

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data['confirm_password']
        original_password = self.cleaned_data['password']
        if original_password != confirm_password:
            raise forms.ValidationError("Password doesn't match")

        return confirm_password

    class Meta:
        model = MyUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логін', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class AddPostForm(forms.ModelForm):
    class Meta:
        model = diary_entries
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'cols': 60, 'rows': 10, 'class': 'form-input'}, )
        }
