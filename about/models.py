from django.db import models
from datetime import datetime

# Create your models here.



class About(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to = 'about/%Y/%m/%d/' , blank=True)
    name = models.CharField(max_length=100)
    
    about_date = models.DateTimeField(default=datetime.now, blank=True)



    def __str__(self):
        return f'{self.name} | {self.title}'


class Skill(models.Model):
    title = models.CharField(max_length=300)
    rate = models.CharField(max_length=20)
    date = models.DateTimeField(default=datetime.now, blank=True)



    def __str__(self):
        return f'{self.title}'