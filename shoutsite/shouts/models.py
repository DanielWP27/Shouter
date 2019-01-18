from django.db import models

class User(models.Model):
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=200)
    reg_date = models.DateTimeField('Date registered')
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)

    def __str__(self):
        return self.username

    def list_shouts(self):
        #verbose
        #shout_list = ", ".join([Shout.objects.filter(user=self.id)])
        shout_list = ", ".join([str(shout.id) for shout in self.shouts.all()])
        return shout_list


class Shout(models.Model):
    shout_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date shouted')
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='shouts')
    #get rid of null & blank at some point
