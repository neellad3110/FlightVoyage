from django.db import connection, models
from accounts.models import User
import uuid
from datetime import datetime,timedelta 
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

        
        if self.pk:
            remark=''

            try:
                current_instance = Flight.objects.get(pk=self.pk)
            except Flight.DoesNotExist:
                current_instance = None

            if current_instance:
                current_instance = Flight.objects.get(pk=self.pk)

                if self.source != current_instance.source and  self.destination != current_instance.destination  and self.departure_date != current_instance.departure_date and self.departure_time != current_instance.departure_time :
                    remark="Attention : Your Booking is cancelled because flight route and departure have been changed, you will receive refund within 24 hours. Thank you for your understanding"
                    
                elif self.source != current_instance.source or self.destination != current_instance.destination:
                    remark="Attention : Your Booking is cancelled because flight route have been changed, you will receive refund within 24 hours. Thank you for your understanding"
                    
                elif self.departure_date != current_instance.departure_date or self.departure_time != current_instance.departure_time:
                    remark="Attention : Your Booking is cancelled because flight departure have been changed, you will receive refund within 24 hours. Thank you for your understanding"


                FlightSeatManager.objects.filter(flight_id=self.id).update(status=0)

                with connection.cursor() as cursor:
                    cursor.execute("update home_userlog set status=-1,is_changed=1,remarks=%s where flight_id=%s and status=1",(remark,self.id,))

            else:
                
                for seat in range(1,self.seats+1):
                    FlightSeatManager.objects.create(flight_id=self.id,seat=seat,status=0)

        departure_datetime = datetime.combine(self.departure_date, self.departure_time)
        self.cancellation_period = departure_datetime - timedelta(hours=24)

        super().save(*args, **kwargs)

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


