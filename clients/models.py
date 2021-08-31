from django.db import models
from datetime import datetime



class Client(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to = 'clients/%Y/%m/%d/' , blank=True)
    jobside = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    client_date = models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return f'{self.name} | {self.title}'