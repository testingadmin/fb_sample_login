from django import forms
from facebookpage.models import UserPerson


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserPerson
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control ml-q'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control ml-q'}),
        }

