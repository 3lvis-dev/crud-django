from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return f'Persona: {self.name} {self.lastname} {self.email}'