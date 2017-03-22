from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# Create your models here.

class EventForm(models.Model):

    food_choices = (('NONVEG', 'Non-Veg'),
                   ('VEG', 'Veg'))
    name_regex = RegexValidator(r'^[a-zA-Z ]*$', message="Please enter a valid name")
    Name = models.CharField(max_length=100, validators=[name_regex])
    Paper_ID = models.IntegerField()
    Title = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|4[987654310]|3[9643210]|2[70]|7|1)\d{1,14}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    Contact = models.CharField(validators=[phone_regex], blank=True, max_length=15) # validators should be a list
    Amount = models.IntegerField()
    Bank = models.CharField(max_length=50)
    Reference_Number = models.IntegerField()
    Date_of_Fee_Deposited = models.DateField()
    Accommodation = models.BooleanField()
    Food_Choice = models.CharField(max_length=10, choices=food_choices)
