from django.db import models

# Create your models here.
class INFORMACION_PERSONAL(models.Model):
    id_datos_personales = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=75)
    dni = models.CharField(max_length=9)
    foto = models.CharField(max_length=255, blank=True, null=True) # Ruta de la foto
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15) # Número de teléfono completo
    telefono_auxiliar = models.CharField(max_length=15, blank=True)
    correo = models.CharField(max_length=50, blank=True)
    correo_ceprunsa = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    class Meta:
        db_table = 'INFORMACIONES_PERSONALES'
        verbose_name = 'INFORMACION_PERSONAL'
        verbose_name_plural = 'INFORMACIONES_PERSONALES'
        ordering = ['id_datos_personales']
    
    def __str__(self):
        return self.nombres + ' ' + self.apellidos
    