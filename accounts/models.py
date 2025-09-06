from django.db import models

class GoodModel(models.Model):
    title = models.CharField(default="good")