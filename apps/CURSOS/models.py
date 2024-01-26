from django.db import models

class CURSO(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = "CURSOS"
        verbose_name = "CURSO"
        verbose_name_plural = "CURSOS"
        ordering = ["id_curso"]
    
    def __str__(self):
        return self.nombre
    


