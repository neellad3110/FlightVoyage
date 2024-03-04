from django.db import models
from accounts.models import User
import uuid
from datetime import datetime,timezone,timedelta 
from django.core.validators import MinValueValidator

# Create your models here.

class Country(models.Model):
    
    id=models.CharField(default=uuid.uuid4,primary_key=True,editable=False)
    name = models.CharField(null=False,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Flight(models.Model):
    
    id=models.CharField(default=uuid.uuid4,primary_key=True,editable=False)
    name = models.CharField(null=False)
    number = models.CharField(null=False,unique=True)
    source = models.ForeignKey(Country, on_delete=models.CASCADE,related_name='source_flights')
    destination = models.ForeignKey(Country, on_delete=models.CASCADE,related_name='destination_flights')
    departure_date = models.DateField(null=False)
    departure_time = models.TimeField(null=False)
    cancellation_period=models.DateTimeField(null=True,blank=True,editable=False)
    seats= models.PositiveIntegerField(validators=[MinValueValidator(1)],null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    def save(self,*args, **kwargs):

        departure_datetime = datetime.combine(self.departure_date, self.departure_time)
        self.cancellation_period = departure_datetime - timedelta(hours=24)

        super().save(*args, **kwargs)
        for seat in range(1,self.seats+1):
            seat_log=FlightSeatManager.objects.create(flight_id=self.id,seat=seat,status=0)


    def __str__(self):
        return f"{self.number} - {self.name}"
class FlightBookinglog(models.Model):

    STATUS_CHOICES = (
        (-1, 'Cancelled'),
        (1, 'Confirmed'),
    )

    id=models.CharField(default=uuid.uuid4,primary_key=True,editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight =models.ForeignKey(Flight,on_delete=models.CASCADE)
    seat= models.IntegerField(null=False)
    status=models.IntegerField(default=0,null=False,choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class FlightSeatManager(models.Model):

    STATUS_CHOICES = (
        (0, 'Pending'),
        (1, 'Confirmed'),
    )

    id=models.CharField(default=uuid.uuid4,primary_key=True,editable=False)
    flight =models.ForeignKey(Flight,on_delete=models.CASCADE)
    seat= models.IntegerField(null=False)
    status=models.IntegerField(default=0,null=False,choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Flight Seat Log"


