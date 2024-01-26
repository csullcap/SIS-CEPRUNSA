from django.db import models

# Create your models here.
class PROCESO(models.Model):
    id_proceso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=70)
    anio_ingreso = models.DateField()
    anio_proceso = models.DateField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    fechas_importantes = models.JSONField()

    class Meta:
        db_table = 'PROCESOS'
        verbose_name = 'PROCESO'
        verbose_name_plural = 'PROCESOS'
        ordering = ['id_proceso']

