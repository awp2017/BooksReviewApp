from django import forms
from ..models import BookRequest


class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class BookRequestForm(forms.ModelForm):
    class Meta(object):
        model = BookRequest
        fields = ['writer','book_name']
