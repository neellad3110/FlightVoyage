from django.db import models
from accounts.models import User
import uuid
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
    departure_tiime = models.TimeField(null=False)
    seats = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class Bookinglog(models.Model):

    id=models.CharField(default=uuid.uuid4,primary_key=True,editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight =models.ForeignKey(Flight,on_delete=models.CASCADE)
    seat_number= models.IntegerField(null=False)
    booking_status=models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)




