
from django.db import models

# Create your models here.

class Value(models.Model):
    ear = models.IntegerField(blank=True, null=True)
    rhand = models.IntegerField(blank=True, null=True)
    lhand = models.IntegerField(blank=True, null=True)
    mouth = models.IntegerField(blank=True, null=True)

class Info(models.Model):
    temp = models.CharField(max_length=11, blank=True, null=True)
    people = models.IntegerField(blank=True, null=True)

class Parameter(models.Model):
    sp1 = models.IntegerField(blank=True, null=True)
    sp2 = models.IntegerField(blank=True, null=True)
    sp3 = models.IntegerField(blank=True, null=True)
    ang1 = models.IntegerField(blank=True, null=True)
    ang2 = models.IntegerField(blank=True, null=True)
    ang3 = models.IntegerField(blank=True, null=True)
    dis1 = models.IntegerField(blank=True, null=True)
    dis2 = models.IntegerField(blank=True, null=True)
    dis3 = models.IntegerField(blank=True, null=True)

class Inventory(models.Model):
    id = models.BigAutoField(primary_key=True)
    finger = models.CharField(db_column='Finger', max_length=50, blank=True, null=True)  # Field name made lowercase.
    identify = models.CharField(db_column='Identify', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inventory'
