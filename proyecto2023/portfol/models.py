from django.db import models

# Create your models here.

class Proyect(models.Model):
	title = models.CharField(max_length=200, verbose_name='Titulo')
	descrition = models.TextField(verbose_name='Descripcion')
	image= models.ImageField(verbose_name='Imagen', upload_to='projects')
	link = models.URLField(verbose_name="Dirección web", null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
	update= models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')




