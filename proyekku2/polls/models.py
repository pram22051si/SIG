from django.db import models


class Provinsi(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    alt_name = models.CharField(max_length=255, default='')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)

    class Meta:
        db_table = 'provinces'
        verbose_name_plural = 'Provinsi'

    def __str__(self):
        return self.name



class Kabkota(models.Model):
    id = models.BigIntegerField(primary_key=True)
    provinsi = models.ForeignKey(Provinsi, on_delete=models.CASCADE, related_name='kabkota',  db_column='province_id')
    name = models.CharField(max_length=255)
    alt_name = models.CharField(max_length=255, default='')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)

    class Meta:
        db_table = 'regencies'
        verbose_name_plural = 'Kabkota'

    def __str__(self):
        return self.name