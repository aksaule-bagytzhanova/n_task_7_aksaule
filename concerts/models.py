from django.db import models
from django.utils import timezone
from users.models import User


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    datetime = models.DateTimeField()
    available_tickets = models.IntegerField()
    total_tickets = models.IntegerField()
    price = models.FloatField() 
    
    def __str__(self):
        return self.title
    
class Booking(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Confirmed', 'Confirmed'),
        ('Returned', 'Returned'),
        
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, max_length=64, default='New')
    
    def __str__(self):
        return f"{self.user} {self.event} {self.status}"

class CalendarIntegration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    #CalendarEventID = 
    sync_time = models.DateTimeField(default=timezone.now)