from django.db import models
from django.contrib.auth.models import User

class Shout(models.Model):
    shout_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField('Date Shouted')
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shouts', verbose_name='Shouter')
'''
class Profile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shouts', verbose_name='Shouter')
    total_likes = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
'''
