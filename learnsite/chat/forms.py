from django import forms
from django.contrib.auth.models import User

class MessageForm(forms.Form):
    text = forms.CharField(label='Текст', widget=forms.TextInput(attrs={'placeholder': 'Ваше повідомлення тут...'}))
    recipient = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())
