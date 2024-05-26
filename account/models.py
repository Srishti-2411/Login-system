from pickle import TRUE
from unicodedata import category
from django.db import models
from distutils.command.upload import upload

from django.contrib.auth.models import AbstractUser
from datetime import datetime 
# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_patient = models.BooleanField('Is patient', default=False)
    is_doctor = models.BooleanField('Is doctor', default=False)








    
    
    





