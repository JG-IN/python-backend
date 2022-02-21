from django.db import models

class HashTag(models.Model):
    message = models.CharField(max_length=100)
# Create your models here.
