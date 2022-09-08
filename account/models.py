from unicodedata import category
from django.db import models
from distutils.command.upload import upload

from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_patient = models.BooleanField('Is patient', default=False)
    is_doctor = models.BooleanField('Is doctor', default=False)

class Category(models.Model):
    cat_id= models.CharField(max_length=10)
    cat_name= models.CharField(max_length=100)

class Blog(models.Model):
    title=models.CharField(max_length=100,blank=True)
    category=models.OneToOneField(Category, on_delete=models.CASCADE)
    summary=models.TextField(blank=True)
    content=models.TextField(blank=True)
    draft=models.BooleanField(blank=True)





