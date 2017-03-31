from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Iba(models.Model):
    iba_id = models.AutoField(primary_key=True)
    iba_code = models.CharField(max_length=10, null=True)
    iba_name = models.CharField(max_length=200)
    pa = models.CharField(max_length=20, null=True)
    criteria = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.iba_code

class Species(models.Model):
    id = models.AutoField(primary_key=True)
    species_id = models.CharField(max_length=10)
    sci_name = models.CharField(max_length=100)
    com_name = models.CharField(max_length=100)
    b_family = models.CharField(max_length=200)
    redlist = models.CharField(max_length=20)

    def __str__(self):
        return self.com_name

class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_code = models.CharField(max_length=3, null=True)
    state_name = models.CharField(max_length=50)
    state_capital = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.state_name + "/" +self.state_code

# class Citie(models.Model):
#     city_id = models.IntegerField(primary_key=True)
#     city_name = models.CharField(max_length=50)
#     latitude = models.IntegerField()
#     longitude = models.IntegerField()
#     state = models.CharField(max_length=50, null=True)


class District(models.Model):
    district_id = models.AutoField(primary_key=True)
    district_name = models.CharField(max_length=50)
    district_state = models.ForeignKey(State)

    def __str__(self):
        return self.district_name


class Bird(models.Model):
    land_choices = (
        ('WETLANDS', 'Wetlands'), ('GALLIFORM', 'Galliform'), ('HERONARY', 'Heronary'), ('TERRESTIAL', 'Terrestial'))
    states = (('WEST BENGAL', 'WEST BENGAL'), ('PUNJAB', 'PUNJAB'), ('TAMILNADU', 'TAMIL NADU'))
    forest_choices = (('Tropical Wet Evergreen Forest', 'Tropical Wet Evergreen Forest'),
                      ('Tropical Semi-Evergreen Forest', 'Tropical Semi-Evergreen Forest'),
                      ('Tropical Moist Deciduous Forest', 'Tropical Moist Deciduous Forest'),
                      ('Littoral and Swamp Forest', ' Littoral and Swamp Forest'),
                      ('Tropical Dry Deciduous Forest', 'Tropical Dry Deciduous Forest'))

    site_choices = (('Coringa and Godaveri Estuary', 'Coringa and Godaveri Estuary'),
                    ('Horsely Hills', 'Horsely Hills'))

    # iba_code = models.CharField(max_length=10, verbose_name='IBA Code')
    iba_code = models.ForeignKey(Iba, verbose_name='IBA Code')
    start_date = models.DateField(verbose_name="From", null=True)
    end_date = models.DateField(verbose_name='Upto', null=True,)
    species = models.ForeignKey(Species)
    area = models.IntegerField(verbose_name='Area in sq.km', default=24000)
    latitude_from = models.FloatField(blank=True, null=True)
    latitude_to = models.FloatField(blank=True, null=True)
    longitude_from = models.FloatField(blank=True, null=True)
    longitude_to = models.FloatField(blank=True, null=True)
    site_name = models.CharField(verbose_name='Site Name', max_length=30, blank=True, null=True, choices=site_choices)
    type_of_location = models.CharField(max_length=50, null=True)
    terrain = models.CharField(max_length=15, blank=True, choices=land_choices)
    breeding_time = models.PositiveIntegerField(verbose_name='Breeding Time(in weeks)', blank=True)
    block_count = models.IntegerField(verbose_name='Block Count')
    forest_type = models.CharField(max_length=50, blank=True, choices=forest_choices)
    # districts = models.ForeignKey(District, null=True)
    state = models.ForeignKey(State, verbose_name="State")

    def __str__(self):
        return str(self.species)

class contribution(models.Model):
    user_id = models.ForeignKey(User)
    contribution_id = models.ForeignKey(Bird)

