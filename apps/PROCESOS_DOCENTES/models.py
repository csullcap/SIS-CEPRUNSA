from django.db import models
from apps.PROCESOS.models import PROCESO
from apps.DOCENTES.models import DOCENTE
from apps.CURSOS.models import CURSO

# Create your models here.
class PROCESO_DOCENTE(models.Model):
    id_proceso_docente = models.IntegerField(primary_key=True)
    id_proceso = models.ForeignKey(PROCESO, models.DO_NOTHING, db_column='id_proceso')
    id_docente = models.ForeignKey(DOCENTE, models.DO_NOTHING, db_column='id_docente')
    id_curso = models.ForeignKey(CURSO, models.DO_NOTHING, db_column='id_curso')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    horas = models.IntegerField()
    horario= models.JSONField()

    class Meta:
        db_table = 'PROCESOS_DOCENTES'
        verbose_name = 'PROCESO_DOCENTE'
        verbose_name_plural = 'PROCESOS_DOCENTES'
        ordering = ['id_proceso_docente']
    
    def __str__(self):
        return str(self.id_proceso_docente)
