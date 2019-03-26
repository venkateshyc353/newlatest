from django.db import models

class schoolapp(models.Model):
    name=models.CharField(max_length=25)
    number=models.IntegerField()
    salary=models.CharField(max_length=20)
    feedback=models.TextField()

    def __str__(self):
        return 'name :{0}\nnumber :{1}\nc :{2}\nfeedback :{3}'.format(self.name,self.number,self.salary,self.feedback)
