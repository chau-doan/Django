from django.db import models

# Create your models here.
class User(models.Model):
  lName = models.CharField(max_length=128)
  fName = models.CharField(max_length=128)
  email = models.EmailField(max_length=264, unique=True) 
  
  
