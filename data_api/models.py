from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User

class Content(models.Model):
    content_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body


class Like(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + ' likes ' + self.content.text_content


class Follow(models.Model):
    follower = models.OneToOneField(User, on_delete=models.CASCADE, related_name='follower_set',primary_key=True)
    followee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followee_set')

    class Meta:
        unique_together = ('follower', 'followee')

    def __str__(self):
        return self.follower.username + ' follows ' + self.followee.username