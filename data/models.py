from django.db import models


# Create your models here.

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

    iba_code = models.CharField(max_length=10, verbose_name='IBA Code')
    # start_date = models.DateField(verbose_name="From", null=True)
    # end_date = models.DateField(verbose_name='Upto', null=True)
    species = models.CharField(max_length=30)
    area = models.IntegerField(verbose_name='Area in sq.km', default=24000)
    latitude_from = models.FloatField(blank=True, null=True)
    latitude_to = models.FloatField(blank=True, null=True)
    longitude_from = models.FloatField(blank=True, null=True)
    longitude_to = models.FloatField(blank=True, null=True)
    site_name = models.CharField(verbose_name='Site Name', max_length=30, blank=True, null=True, choices=site_choices)
    terrain = models.CharField(max_length=15, blank=True, choices=land_choices)
    breeding_time = models.PositiveIntegerField(verbose_name='Breeding Time(in weeks)', blank=True)
    block_count = models.IntegerField(verbose_name='Block Count')
    forest_type = models.CharField(max_length=50, blank=True, choices=forest_choices)
    districts = models.CharField(max_length=20, blank=True)
    state = models.CharField(max_length=15, choices=states)

    def __str__(self):
        return self.species
