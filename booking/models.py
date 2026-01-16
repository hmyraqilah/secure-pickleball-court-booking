from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class CourtBooking(models.Model):
    COURT_CHOICES = [
        (1, "Court 1"),
        (2, "Court 2"),
        (3, "Court 3"),
        (4, "Court 4"),  # add as many as your facility has
    ]
    
    court_number = models.IntegerField(choices=COURT_CHOICES, default=1)
    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Court {self.court_number} booked by {self.user.username} on {self.date} at {self.time}"
    

