from django.db import models

# Create your models here.


class Datos(models.Model):

    fecha = models.DateField('Fecha')
    concepto = models.CharField('Concepto', max_length=200)
    ingreso = models.FloatField('Ingreso', default=0.0)
    gasto = models.FloatField('Gasto', default=0.0)
    total = models.FloatField('Total', default=0.0)

    class Meta:
        verbose_name = 'Dato'
        verbose_name_plural = 'Datos'

        ordering = ['-fecha']

    def __str__(self):
        return str(self.fecha) + ' ' + self.concepto


