from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class LocationModel(models.Model):
    name = models.CharField(max_length=120, blank=False, unique=True)

    def __str__(self):
        return self.name

class WorkTypeModel(models.Model):
    name = models.CharField(blank=False, max_length=120, unique=True)

    def __str__(self):
        return self.worktype

class UserModel (models.Model):
    usertype = models.CharField(max_length=10,default=None)
    first_name = models.CharField(max_length=200, default=None)
    last_name = models.CharField( max_length=200, default=None)
    company_name = models.CharField( max_length=200, default=None)
    password = models.CharField(max_length=300, default=None)             
    email = models.EmailField(blank=False, unique=True)
    phone = models.CharField(max_length=120, blank=False, unique=True)
    register_date = models.DateTimeField(max_length=100, default=timezone.now)
    image = models.CharField(max_length=200, default=None)
    location = models.ForeignKey(LocationModel, blank=False, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.first_name + " " + "is a" + self.usertype

class WorkersModel(models.Model):

    availability = models.BooleanField(default=True)
    charge = models.IntegerField(default=100)
    charge_type = models.CharField(max_length=20,default=None)
    experience = models.CharField(max_length=30, default=None)
    work_description = models.TextField(default=None)
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE, blank=False)
    worktype = models.ForeignKey(WorkTypeModel, blank=False, on_delete=models.SET_NULL, null=True)

class SeekersModel(models.Model):
    job_description = models.TextField(default=None)
    duration = models.CharField( max_length=30)
    worktype = models.ForeignKey(WorkTypeModel,blank=False, on_delete=models.SET_NULL,null=True)
    image = models.CharField(max_length=1000)
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE, blank=False, default=None)

class ConnectionModel(models.Model):
    seeker_id = models.ForeignKey(SeekersModel,blank=False, on_delete=models.SET_NULL, null=True)
    worker_id = models.ForeignKey(WorkersModel,blank=False, on_delete=models.SET_NULL, null=True)
    likes = models.PositiveIntegerField(default=0)
    comments = models.TextField(default=None)

    class Meta:
        unique_together = ("seeker_id", "worker_id",)
