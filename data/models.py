from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Iba(models.Model):
    iba_id = models.AutoField(primary_key=True)
    iba_code = models.CharField(max_length=10, null=True)
    iba_name = models.CharField(max_length=200)
    pa = models.CharField(max_length=20, null=True)
    criteria = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.iba_code

class Specie(models.Model):
    pass

class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_code = models.CharField(max_length=3, null=True)
    state_name = models.CharField(max_length=50)
    state_capital = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.state_name + "/" + self.state_code


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


class Observation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    timestamp = models.DateTimeField('date published', default=timezone.now())
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    iba_code = models.ForeignKey(Iba)
    start = models.DateTimeField()
    duration = models.IntegerField()
    protocol_type = models.CharField(max_length=50)
    trip_comments = models.CharField(max_length=200)


class contribution(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL)
    contribution_id = models.ForeignKey(Observation)
