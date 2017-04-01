from django.db import models


# Create your models here.\

class family(models.Model):
    f_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        self.name


class redlist(models.Model):
    r_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5, null=True)

    def __str__(self):
        self.name


class habitat(models.Model):
    h_id = models.AutoField(primary_key=True)
    habitat = models.CharField(max_length=50)

    def __str__(self):
        self.habitat


class iba_status(models.Model):
    is_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        self.name


class criteria(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_code = models.CharField(max_length=8)
    description = models.CharField(max_length=200)

    def __str__(self):
        self.c_code +"/"+ self.description


class state(models.Model):
    st_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=50)
    capital = models.CharField(max_length=50)
    # area = models.IntegerField()
    # forest_area = models.IntegerField()

    def __str__(self):
        self.name+"/"+self.code


class district(models.Model):
    d_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    state = models.ForeignKey(state)

    def __str__(self):
        self.name


class specie(models.Model):
    s_id = models.AutoField(primary_key=True)
    sprec_id = models.CharField(max_length=10)
    sci_name = models.CharField(max_length=100)
    com_name = models.CharField(max_length=100)
    family = models.ForeignKey(family)
    redlist = models.ForeignKey(redlist)

    def __str__(self):
        self.com_name


class iba(models.Model):
    iba_id = models.AutoField(primary_key=True)
    iba_code = models.CharField(max_length=50)
    site_name = models.CharField(max_length=50)
    state = models.ForeignKey(state)
    area = models.FloatField(null=True)
    status = models.ForeignKey(iba_status)

    def __str__(self):
        self.iba_code


class district_iba(models.Model):
    iba = models.ForeignKey(iba)
    district = models.ForeignKey(district)


class criteria_iba(models.Model):
    iba = models.ForeignKey(iba)
    citeria = models.ForeignKey(criteria)


class habitat_iba(models.Model):
    iba = models.ForeignKey(iba)
    habitat = models.ForeignKey(habitat)
