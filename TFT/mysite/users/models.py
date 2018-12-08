from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from phone_field import PhoneField



GENGER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
]
TYPE_CHOICES = [
    ('restaurant and coffee shop', 'restaurant and coffee shop'),
    ('Cinemas and theaters and concerts', 'Cinemas and theaters and concerts'),
    ('Amusement Park', 'Amusement Park'),
    ('shopping center', 'shopping center'),
    ('female', 'Sports'),
    ('Park and free space', 'Park and free space'),
    ('Other', 'Other'),
]

class Interest(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    address = models.CharField(max_length=60, unique=False, blank=True, help_text='Optional', default='')
    phone_number = PhoneField(blank=False, help_text='Contact phone number', default='')
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENGER_CHOICES, default='STRING')
    favorites = models.ManyToManyField(Interest, related_name='favorited_by')
    center_manager=models.BooleanField(default=False,help_text='Select if you own a center and you want to register it on our site')
    def __str__(self):
        return self.email

class UserInterests(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, unique=False, on_delete=models.DO_NOTHING)
    interest = models.ForeignKey(Interest, unique=True, on_delete=models.DO_NOTHING)
    def __unicode__(self):
        return self.user.username





class Center(models.Model):
    name = models.CharField(max_length=100, unique=False, blank=True)
    address = models.CharField(max_length=250)
    phone_number = PhoneField(blank=False, help_text='Contact phone number', default='')
    email= models.EmailField()
    type=models.CharField(max_length=100, choices=TYPE_CHOICES, default='STRING')
    ticket_cost=models.IntegerField(help_text='In Toman')
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.name


class CenterHours(models.Model):
    center_id=models.ForeignKey(Center, unique=False, on_delete=models.DO_NOTHING)
    day=models.CharField(max_length=100)
    open_time=models.CharField(max_length=100)
    close_time=models.CharField(max_length=100)



class ManagerCenters(models.Model):
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, unique=False, on_delete=models.DO_NOTHING)
    center = models.ForeignKey(Center, unique=True, on_delete=models.DO_NOTHING)
    def __unicode__(self):
        return self.user.username

