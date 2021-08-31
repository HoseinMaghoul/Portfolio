from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to = 'blogs/%Y/%m/%d/' , blank=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    is_published = models.BooleanField(default = False)


    def __str__(self):
        return f'{self.title}-{self.user}'