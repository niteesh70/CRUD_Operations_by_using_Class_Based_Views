from django.db import models

# Create your models here.
from django.urls import reverse

class School(models.Model):
    sname=models.CharField(max_length=100)
    sprincipal=models.CharField(max_length=100)
    slocaction=models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.sname



class Student(models.Model):
    stname=models.CharField(max_length=100)
    stage=models.IntegerField()
    sname=models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')


    def __str__(self):
        return self.stname
