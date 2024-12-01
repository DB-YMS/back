from django.db import models

import location.models


# Create your models here.


class Driver(models.Model):
    driver_id = models.CharField(primary_key=True, max_length=10)
    division = models.ForeignKey(location.models.Division, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'driver'
