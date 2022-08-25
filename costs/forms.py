from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from costs.models import CustomUser


class DataSearch(forms.Form):
    data = forms.DateField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Пошук по даті..."})
    )


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
