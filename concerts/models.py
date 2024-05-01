from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    datetime = models.DateTimeField()
    availabletickets = models.IntegerField()
    totaltickets = models.IntegerField()
    price = models.FloatField() 
    
class Users(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    email = models.CharField(max_length=255)
    
class Booking(models.Model):
    STATUS = (
        ('Confirmed', 'Confirmed'),
        ('Returned', 'Returned'),
        
    )
    UserID = models.ForeignKey(Users)
    EventID = models.ForeignKey(Event)
    NumberOfTickets = models.IntegerField()
    BookingDate = models.DateTimeField()
    Status = models.CharField(choices=STATUS)

class CalendarIntegration(models.Model):
    UserID = models.ForeignKey(Users)
    EventID = models.ForeignKey(Event)
    #CalendarEventID = 
    SyncTime = models.DateTimeField(default=timezone.now)