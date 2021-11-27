from django import forms
from django.core.mail import send_mail 


class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100, required=True)
    from_email = forms.EmailField(max_length=100, required=True)
    assunto = forms.CharField(max_length=100, required=True)
    mensagem = forms.CharField(widget=forms.Textarea(), required=True)