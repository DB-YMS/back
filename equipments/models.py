from django.db import models

class Equipment(models.Model):
    equipment_id = models.CharField(primary_key=True, max_length=4)
    equipment_type = models.CharField(max_length=10)
    equipment_sort = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    id = models.ForeignKey('location.Master', models.DO_NOTHING, db_column='id')

    class Meta:
        managed = False
        db_table = 'equipment'