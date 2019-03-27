from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=20)

    def __str__(self):
        return self.name
class Furniture_Model(models.Model):
    front_view = models.CharField(max_length=50)
    side_view = models.CharField(max_length=50)
    position = models.CharField(max_length=20)
    type = models.CharField(max_length=20)