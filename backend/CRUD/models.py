from django.db import models

# Create your models here.

class Post(models.Model):
    # user = 
    body_text = models.CharField(max_length=150)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add = True)

