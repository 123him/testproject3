from django.db import models

# Create your models here.
class tbl_user(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    class Meta:
        db_table ="tbl_user"