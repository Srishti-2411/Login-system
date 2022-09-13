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

class Category(models.Model):
    cat_id= models.CharField(max_length=10)
    cat_name= models.CharField(max_length=100)

class Blog(models.Model):
    title=models.CharField(max_length=100,blank=True)
    category=models.OneToOneField(Category, on_delete=models.CASCADE)
    summary=models.TextField(blank=True)
    content=models.TextField(blank=True)
    draft=models.BooleanField(blank=True)

class Speciality(models.Model):
    spe_id=models.CharField(max_length=100)
    spe_name=models.CharField(max_length=100)


class Appointment(models.Model):
    required_speciality=models.OneToOneField(Speciality,on_delete=models.CASCADE)
    Appointment_date = models.DateField(default=datetime.now, blank=True)
    Appointment_time=models.TimeField(auto_now_add=True,null=True,blank=True)

    def get_date(self):
        time=datetime.now()

        if self.date.day== time.day:
            return str(time.hour -self.date.hour) 
        else:
            if self.month== time.month:
                return str(time.day - self.date.day)

        return self.date
    
    
    





