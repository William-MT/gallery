from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(null=True)
    category = models.CharField(max_length=20)
    provider = models.CharField(max_length=200)
    date = models.DateField(null=True)
    netstatus = models.CharField(max_length=20, null=True)
