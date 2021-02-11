from django.db import models
from django.utils import timezone

class Post1(models.Model):
    username = models.CharField(max_length=200,  blank=True ,null=False)
    title = models.CharField(max_length=200,default="hiiiiii", blank=True ,null=False)
    text = models.TextField()
    image1 = models.ImageField(upload_to='blogsite/static/images/')
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title},{self.text},{self.image1}'







