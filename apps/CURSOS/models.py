from django.db import models

class CURSOS(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)



