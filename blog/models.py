from django.db import models

class BlogSpot(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()