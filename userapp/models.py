from django.db import models

# Create your models here.
class userregi (models.Model):
    Fullname = models.TextField(max_length=30)
    Phonenumber = models.CharField(max_length=15)
    Address = models.TextField(max_length=250)
    Email = models.EmailField()
    Password = models.CharField(max_length=25)
    Uploadid = models.FileField(upload_to='pic')
