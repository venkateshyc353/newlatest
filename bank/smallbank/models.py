from django.db import models


class person(models.Model):
    firstname=models.CharField(max_length=55)
    lastname=models.CharField(max_length=50)
    # def __str__(self):
    #     return 'firstname..... {0} lastname....{1} '.format(self.firstname,self.lastname)
