from django.db import models

# Create your models here.

class mytodods(models.Model):
    title = models.CharField(max_length=120)
    desc = models.TextField()
    image  = models.ImageField(upload_to="images", null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)