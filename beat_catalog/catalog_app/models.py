from django.db import models

# Create your models here.

class Beat(models.Model):
    number = models.IntegerField()
    name = models.TextField()
    bpm = models.IntegerField()
    key = models.TextField()
    full_path = models.TextField()
    del_field = models.TextField(default="delete")