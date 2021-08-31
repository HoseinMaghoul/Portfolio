from django.db import models
from datetime import datetime

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=254)
    text = models.TextField(max_length=1000)
    date = models.DateTimeField(default=datetime.now, blank=True)



    def __str__(self):
        return f'{self.name}-{self.text[:20]}'



