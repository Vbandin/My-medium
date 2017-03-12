# -*- coding: utf-8 -*-
from django import forms

class LoginForm(forms.Form):
    username = forms.Field()
    password = forms.Field(widget=forms.PasswordInput())