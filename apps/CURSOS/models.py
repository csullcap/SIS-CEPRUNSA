from django.db import models
#import apps.DOCENTES.models as DOCENTES 

class CURSOS(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    #id_docente = models.ForeignKey(DOCENTES, models.DO_NOTHING, db_column='id_docente')


