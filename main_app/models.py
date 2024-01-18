from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

# Create your models here.

WORKOUTS = (

    ('R', 'Reps'),
    ('S', 'Sets'),

)

class Journey(models.Model):
    TYPE_CHOICES = [
        ('CARDIO', 'Cardio'),
        ('STRENGTH', 'Strength training'),
        ('FLEXIBILITY', 'Flexibility exercise'),
        ('BALANCE', 'Balance exercise'),
        ('HIIT', 'High-Intensity Interval Training'),
        ('CIRCUIT', 'Circuit Training'),
        ('OTHER', 'Other')
    ]
    
    # Basic information
    name = models.CharField(max_length=100)
    workout_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    description = models.TextField()
    
    # Timing information
    date = models.DateField()
    start_time = models.TimeField()

    #adding journey to user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse('detail', kwargs={'journey_id': self.id})

class RepSet(models.Model):
    rep = models.CharField(
        max_length=99,
        choices=WORKOUTS,
        default=WORKOUTS[0][0]
        )
    set = models.CharField(
        max_length=99,
        choices=WORKOUTS,
        default=WORKOUTS[1][1]
        )
    
journey = models.ForeignKey(Journey, on_delete = models.CASCADE)

def __str__(self):
    return f"{self.get_workout_display()} on {self.rep}"

def __str__(self):
    return f'{self.name} ({self.id})'

def get_absolute_url(self):
    return reverse('detail', kwargs={'cat_id':self.id})


