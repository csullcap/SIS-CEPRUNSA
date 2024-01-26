from django.db import models

class tipo_pago_enum(models.TextChoices):
    RXH = 'RXH', ('Recibo por honorarios')
    NOMBRADO = 'NOMBRADO', ('Nombrado')
    CONTRATADO = 'CONTRATADO', ('Contratado')

# Create your models here.
class DATOS_PAGO(models.Model):
    id_datos_pago = models.AutoField(primary_key=True)
    ruc= models.CharField(max_length=11)
    tipo_pago= models.CharField(max_length=10, choices=tipo_pago_enum.choices, default=tipo_pago_enum.RXH)
    titulo_profesional = models.CharField(max_length=50)
    entidad_bancaria = models.CharField(max_length=15)
    numero_cuenta = models.CharField(max_length=20)
    cci= models.CharField(max_length=20)
    suspension_cuarta = models.BooleanField(default=True)
    cv_doc= models.CharField(max_length=255) #link
    cv_documentado_doc= models.CharField(max_length=255) #link
    titulo_doc= models.CharField(max_length=255) #link
    dni_doc= models.CharField(max_length=255) #link

    class Meta:
        db_table = 'DATOS_PAGOS'
        verbose_name = 'DATOS_PAGO'
        verbose_name_plural = 'DATOS_PAGOS'
        ordering = ['id_datos_pago']

    def __str__(self):
        return self.id_datos_pago