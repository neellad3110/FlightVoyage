from django.db import models
from accounts.models import User
from flights.models import Flight,FlightSeatManager,FlightBookinglog
import uuid
from django.core.validators import MinValueValidator
# Create your models here.

class Userlog(models.Model):
    """Model class for User log"""

    STATUS_CHOICES = (
        (-1, 'Cancelled'),
        (1, 'Confirmed'),
    )

    id=models.CharField(default=uuid.uuid4,primary_key=True,editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight =models.ForeignKey(Flight,on_delete=models.CASCADE)
    seat= models.PositiveIntegerField(validators=[MinValueValidator(1)],null=False)
    status=models.IntegerField(default=0,null=False,choices=STATUS_CHOICES)
    is_changed=models.IntegerField(default=0,null=False)
    remarks=models.CharField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def save(self,*args, **kwargs):

        """
            Saves the instance and creates corresponding records in FlightBookinglog and FlightSeatManager.

            When saving the instance, creates a new record in FlightBookinglog with user, flight, seat, and status details.
            Updates the status of the corresponding seat in FlightSeatManager based on the status of the booking.
        """

        FlightBookinglog.objects.create(user_id=self.user_id,flight_id=self.flight_id,seat=self.seat,status=self.status)

        flight_log=FlightSeatManager.objects.get(flight_id=self.flight_id,seat=self.seat)
        if self.status == 1:
            flight_log.status=1
        else: 
            flight_log.status=0

        flight_log.save() 

        super().save(*args, **kwargs)
              
    def __str__(self) -> str:
        return "Update User log"
