from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms import fields

from django.core.exceptions import ValidationError


class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def clean_email(self):
        v_email = self.cleaned_data['email']

        if User.objects.filter(email=v_email).exists():
            raise ValidationError("o email {} já existe registro com usuário".format(v_email))
        
        return v_email



