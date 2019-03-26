from django.db import models
from rest_framework import viewsets


class schoolnames(models.Model):
    name=models.CharField(max_length=50)
    father=models.CharField(max_length=50)
    def __str__(self):
        return '{0}............{1}'.format(self.name,self.father)

# class restapi(viewsets.ModelViewSet):
#     queryset =
