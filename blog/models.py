from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField(max_length=200,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)