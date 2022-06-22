from django import forms
from facebookpage.models import UserPerson


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserPerson
        fields = ['name', 'password']
