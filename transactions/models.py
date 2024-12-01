from django.db import models

import equipments.models
import location.models


# Create your models here.


class Transaction(models.Model):
    transaction_id = models.FloatField(primary_key=True)
    equipment = models.ForeignKey(equipments.models.Equipment, models.DO_NOTHING)
    driver_id = models.CharField(max_length=10)
    from_master = models.ForeignKey(location.models.Master, models.DO_NOTHING)
    to_master = models.ForeignKey(location.models.Master, models.DO_NOTHING, related_name='transaction_to_master_set')
    timestamp = models.IntegerField()
    details = models.TextField()

    class Meta:
        managed = False
        db_table = 'transaction'