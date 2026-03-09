from django.db import models
from django.contrib.auth.models import Group,User

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Event(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    date=models.DateField()
    time=models.TimeField()
    location=models.CharField(max_length=20)
    category=models.ForeignKey(Category,on_delete=models.CASCADE, related_name='event')
    organizer=models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_event',default=1)
    participant=models.ManyToManyField(User,blank=True,related_name="rsvp_event")
    image=models.ImageField(upload_to="event/",blank=True,null=True)
    
    
    def __str__(self):
        return self.name
    
   
# class Participant(models.Model):
#     name=models.CharField(max_length=50)
#     email=models.CharField(max_length=50)
#     event=models.ManyToManyField(Event)
    
#     def __str__(self):
#         return self.name