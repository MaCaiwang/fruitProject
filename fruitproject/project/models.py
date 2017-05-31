from django.db import models

# Create your models here.
class userInfo(object):
    uName = models.CharField(max_length=20)
    uPassword = models.CharField(max_length=20)
    uEmail = models.CharField(max_length=30)
    uShou = models.CharField(max_length=20, default='')
    uAddress = models.CharField(max_length=100, default='')
    uYoubian = models.CharField(max_length=6, default='')
    yPhone = models.CharField(max_length=11, default='')