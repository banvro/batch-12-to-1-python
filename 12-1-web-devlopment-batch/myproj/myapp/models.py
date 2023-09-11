from django.db import models

# Create your models here.
# use to carete and manages tables


class StudentsInfo(models.Model):
    stu_id = models.IntegerField()
    stu_f_name = models.CharField(max_length = 30)
    stu_l_name = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    stu_message = models.TextField()




# migrations

# migrate
