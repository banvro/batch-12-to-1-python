from django.db import models

# Create your models here.

# create table
class ContactUs(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    phone_number = models.IntegerField()
    address = models.CharField(max_length = 100)
    message = models.TextField()


# python manage.py makemigrations

# python manage.py migrate