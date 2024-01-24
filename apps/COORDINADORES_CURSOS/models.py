from django.db import models
from apps.DOCENTES.models import DOCENTES
from apps.CURSOS.models import CURSOS

class estado_enum(models.TextChoices):
    ACTIVO = "ACTIVO"
    FINALIZADO = "FINALIZADO"

# Create your models here.
class COORDINADORES_CURSOS(models.Model):
    id_coordinador_curso = models.AutoField(primary_key=True)
    id_curso = models.ForeignKey(CURSOS, models.DO_NOTHING, db_column="id_curso")
    id_coordinador = models.ForeignKey(DOCENTES, models.DO_NOTHING, db_column="id_docente")
    estado = models.CharField(max_length=10, choices=estado_enum.choices, default=estado_enum.ACTIVO)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    #mediumtext
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "COORDINADORES_CURSOS"
        verbose_name = "COORDINADOR_CURSO"
        verbose_name_plural = "COORDINADORES_CURSOS"
        ordering = ["id_coordinador_curso"]
    
    def __str__(self):
        return self.id_coordinador_curso
