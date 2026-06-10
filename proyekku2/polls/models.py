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
    
 
class Namadata(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'namadata'
        verbose_name = 'Nama Data'
        verbose_name_plural = 'Nama Data'

    def __str__(self):
        return self.name


class Datprof(models.Model):
    provinsi = models.ForeignKey(
        Provinsi,
        db_column='province_id',
        on_delete=models.CASCADE,
        verbose_name="Provinsi"
    )
    namadata = models.ForeignKey(
        Namadata,
        db_column='namadata_id',
        on_delete=models.CASCADE,
        verbose_name="Nama Data"
    )
    tahun = models.IntegerField(verbose_name="Tahun")
    jumlah = models.FloatField(verbose_name="Jumlah")  # PostgreSQL Double Precision dipetakan ke FloatField di Django

    class Meta:
        db_table = 'data_province'  # Menghubungkan model langsung ke tabel PostgreSQL yang sudah ada
        verbose_name = 'Data Provinsi'
        verbose_name_plural = 'Data Provinsi'

    def __str__(self):
        return f"{self.namadata} - {self.provinsi} ({self.tahun})"
