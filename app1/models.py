from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=250)
    category = models.CharField(max_length=20)
    provider = models.CharField(max_length=200)
    date = models.DateField(null=True)
