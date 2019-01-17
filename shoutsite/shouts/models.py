from django.db import models

class Shout(models.Model):
    shout_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date shouted')
    likes = models.IntegerField(default=0)

class User(models.Model):
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=200)
    reg_date = models.DateTimeField('Date registered')
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)

    def __str__(self):
        return self.username
