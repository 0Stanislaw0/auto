from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Profile
from django import forms
from django.utils.translation import ugettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


''' Формы создания  и изменения '''


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class UserOurRegistration(UserCreationForm):
    email = forms.EmailField(label=_('Email'), widget=forms.TextInput(attrs={"class": "myfield"}))
    password1 = forms.CharField(label=_('Password'), min_length=8, widget=forms.TextInput(attrs={"class": "myfield"}))
    password2 = forms.CharField(label=_('Confirm the password '), min_length=8,
                                widget=forms.TextInput(attrs={"class": "myfield"}))
    phone_number = forms.CharField(label=_('Phone number'), min_length=8, max_length=15,
                                   widget=forms.TextInput(attrs={"class": "myfield"}))

    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2', 'phone_number', ]


class UserUpdateForm(forms.ModelForm):
    # email = forms.EmailField(label=_('Email'),widget=forms.TextInput(attrs={"class": "myfield"}))
    # name = forms.CharField(label=_('Name'),min_length=3, widget=forms.TextInput(attrs={"class": "myfield"}))
    # phone_number = forms.CharField(label=_('Phone number'),widget=forms.TextInput(attrs={"class": "myfield"}))
    # location = forms.CharField(label=_('Location'),widget=forms.TextInput(attrs={"class": "myfield"}))

    class Meta:
        model = Profile
        fields = ['first_name', 'location']
