from django.db import models
from apps.CURSOS.models import CURSOS
from apps.DATOS_PERSONALES.models import DATOS_PERSONALES
# Create your models here.
class DOCENTES(models.Model):
    id_docente = models.AutoField(primary_key=True)
    id_curso = models.ForeignKey(CURSOS, models.DO_NOTHING, db_column='id_curso')
    #id_datos_pago = models.ForeignKey('DATOS_PAGO', models.DO_NOTHING, db_column='id_datos_pago')
    id_datos_personales = models.ForeignKey(DATOS_PERSONALES, models.DO_NOTHING, db_column='id_datos_personales')
    
