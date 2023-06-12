from django.db import models
from django.contrib.auth.models import User

# # Create your models here.
# class Users(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     password = models.CharField(max_length=25)

#     def __str__(self):
#         return self.first_name + ' ' + self.last_name

class Topic(models.Model):
    name = models.CharField(max_length=30)
    creator = models.OneToOneField(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_activity = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=30)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
