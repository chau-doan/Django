from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput())

  class Meta(): # connect to models app base default
    model = User
    fields = ('username','email', 'password') 

class UserProfileInfoForm(forms.ModelForm):
  class Meta(): # from userprofileinfo
    model = UserProfileInfo
    fields = ('portfolio_site', 'profile_pic')
