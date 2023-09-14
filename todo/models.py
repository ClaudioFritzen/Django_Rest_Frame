from django.db import models

# Create your models here.
class React(models.Model):
    empregado = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50)
    