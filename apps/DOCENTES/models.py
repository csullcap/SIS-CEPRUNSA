from django.db import models
from apps.CURSOS.models import CURSO
from apps.INFORMACIONES_PERSONALES.models import INFORMACION_PERSONAL
from apps.DATOS_PAGOS.models import DATOS_PAGO

# Create your models here.
class DOCENTE(models.Model):
    id_docente = models.AutoField(primary_key=True)
    id_curso = models.ForeignKey(CURSO, models.DO_NOTHING, db_column='id_curso')
    id_datos_pago = models.ForeignKey(DATOS_PAGO, models.DO_NOTHING, db_column='id_datos_pago')
    id_datos_personales = models.ForeignKey(INFORMACION_PERSONAL, models.DO_NOTHING, db_column='id_datos_personales')

    class Meta:
        db_table = 'DOCENTES'
        verbose_name = 'DOCENTE'
        verbose_name_plural = 'DOCENTES'
        ordering = ['id_docente']

    def __str__(self):
        return self.id_docente