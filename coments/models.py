from django.db import models


class User(models.Model):
    mail = models.EmailField()
    password = models.CharField(max_length=200)


class Message(models.Model):
    user = models.CharField(max_length=256)
    message = models.CharField(max_length=256)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)