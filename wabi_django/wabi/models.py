from crypt import methods
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    # pass
    # name = models.CharField(max_length=100)
    # email = models.CharField(
    #     verbose_name='email address', max_length=255, unique=True)
    # username = models.CharField(max_length=100, null=True)
    # password = models.CharField(max_length=100,)
    # is_active = models.BooleanField(default=)
    friends = models.ManyToManyField(
        'self', through='Friends', blank=True)

# class Friend(models.Model):
#     users = models.ManyToManyField(User)
#     current_user = models.ForeignKey(
#         User, related_name='friends', null=True, on_delete=models.CASCADE)

#     def __str__(self):
#         return str(self.current_user)


class Friends(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="friends_with", null=True)
    friend = models.ForeignKey(User,
                               on_delete=models.CASCADE, related_name="friends_to", null=True)


class Prompt(models.Model):
    date = models.DateField()
    text = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.text


class Sketch(models.Model):
    sketch_data = models.JSONField()
    date = models.DateField(null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sketches', null=True)
    prompt = models.ForeignKey(
        Prompt, on_delete=models.CASCADE, related_name='sketches', null=True)
