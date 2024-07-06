from django.db import models

# Son clases que nos ayudan a gestionar la conexion en la base de datos

#Ponemos el nombre de la tabla, en este caso la tabla se llama 'Pokemon'
#NO necesitamos iniciar con los constructores
class Pokemon(models.Model):
    name = models.CharField(max_length=30, null=False)
    type = models.CharField(max_length=30, null=False)
    weight = models.IntegerField(null=False)
    height = models.IntegerField(null=False)    
    
    def __str__(self) -> str:
        return self.name
