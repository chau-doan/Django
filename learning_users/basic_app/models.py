from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

  # no have user same name
  user = models.OneToOneField(User, on_delete=models.CASCADE)

  #additional
  portfolio_site = models.URLField(blank=True)

  profile_pic = models.ImageField(upload_to='profile_pics', blank=True) # in media folder we need the pillow

  def __str__(self):
    return self.user.username


