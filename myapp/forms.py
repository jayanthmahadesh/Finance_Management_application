from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class new_user_form(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2')
class user_login_form(AuthenticationForm):
    class Meta:
        model = User
        feilds = ['username','password']