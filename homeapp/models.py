from django.db import models

# Create your models here.
class adminlog (models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=25)