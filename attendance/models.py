from django.utils import timezone
from django.db import models

# Create your models here.

class Farmer(models.Model):
    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male'),
    ]
    CONTRACT_CHOICES = [
        ('CASUAL', 'Casual'),
        ('PERMANENT', 'Permanent'),
        ('TEMPORARY', 'Temporary'),
    ]

    name = models.CharField(max_length=50)
    farm = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True,null=True, blank=True)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)      
    contract = models.CharField(max_length=10, choices=CONTRACT_CHOICES)  

    class Meta:
        db_table = "farmer"
# avoid seeing object1 or object 2 but the propeer name of the farmer
    def __str__(self):
        return self.name


class Attendance(models.Model):
    farmer=models.ForeignKey(Farmer,on_delete=models.CASCADE)
    date=models.DateField(default=timezone.now())
    is_present=models.BooleanField(default=False)

    class Meta:
        db_table="attendance"

    