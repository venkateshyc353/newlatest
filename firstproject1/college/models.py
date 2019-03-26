from django.db import models

class college(models.Model):
    name=models.CharField(max_length=25)
    number=models.IntegerField()
    def __str__(self):
        return '{0}{1}'.format(self.name,self.number)