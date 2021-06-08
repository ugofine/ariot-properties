from django.db import models
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=250)
    photo = models.ImageField(upload_to="photo/%Y/%m/%d")
    content = models.TextField()
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    author = models.CharField(max_length=100, default="Admin")

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=250)
    body = models.TextField()
    created_date = models.DateTimeField(default=datetime.now)
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)


    def __str__(self):
        return self.body

