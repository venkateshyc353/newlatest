from django.db import models
class schoolmodel(models.Model):
    name=models.CharField(max_length=250)
    mobile=models.IntegerField()
    addres=models.CharField(max_length=250)
    salary=models.IntegerField()
    surname=models.CharField(max_length=50)
# import matplotlib