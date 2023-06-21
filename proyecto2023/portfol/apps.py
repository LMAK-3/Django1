from django.apps import AppConfig


class PortfolConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfol'
    verbose_name = 'Portafolio'

    class Meta:
    	verbose_name='proyecto'
    	verbose_name_plural= 'proyectos'
    	ordering = ['-created']

    def __str__(self):
    	return self.title
    		
