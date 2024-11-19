# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Division(models.Model):
    division_id = models.IntegerField(primary_key=True)
    division_name = models.CharField(unique=True, max_length=4)

    class Meta:
        managed = False
        db_table = 'division'


class Driver(models.Model):
    driver_id = models.CharField(primary_key=True, max_length=10)
    division = models.ForeignKey(Division, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'driver'


class Equipment(models.Model):
    equipment_id = models.CharField(primary_key=True, max_length=4)
    equipment_type = models.CharField(max_length=10)
    equipment_sort = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    id = models.ForeignKey('Master', models.DO_NOTHING, db_column='id')

    class Meta:
        managed = False
        db_table = 'equipment'


class Master(models.Model):
    id = models.BigIntegerField(primary_key=True)
    division_name = models.ForeignKey(Division, models.DO_NOTHING, db_column='division_name', to_field='division_name')
    yard = models.ForeignKey('Yard', models.DO_NOTHING)
    site = models.ForeignKey('Site', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'master'


class Site(models.Model):
    site_id = models.IntegerField(primary_key=True)
    equipment_type = models.ForeignKey(Equipment, models.DO_NOTHING, db_column='equipment_type')
    capacity = models.IntegerField()
    current_quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'site'


class Transaction(models.Model):
    transaction_id = models.FloatField(primary_key=True)
    equipment = models.ForeignKey(Equipment, models.DO_NOTHING)
    driver_id = models.CharField(max_length=10)
    from_master = models.ForeignKey(Master, models.DO_NOTHING)
    to_master = models.ForeignKey(Master, models.DO_NOTHING, related_name='transaction_to_master_set')
    timestamp = models.IntegerField()
    details = models.TextField()

    class Meta:
        managed = False
        db_table = 'transaction'


class Yard(models.Model):
    yard_id = models.CharField(primary_key=True, max_length=5)

    class Meta:
        managed = False
        db_table = 'yard'
