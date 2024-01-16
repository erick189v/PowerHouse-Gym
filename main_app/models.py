from django.db import models

# Create your models here.
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