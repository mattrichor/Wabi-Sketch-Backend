from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(
        verbose_name='email address', max_length=255, unique=True)
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100,)
    is_active = models.BooleanField(default=False)
    friends = models.ManyToManyField(
        'self', related_name='friends', blank=True)

    def __str__(self) -> str:
        return self.name


# class Friend(models.Model):
#     users = models.ManyToManyField(User)
#     current_user = models.ForeignKey(
#         User, related_name='friends', null=True, on_delete=models.CASCADE)

#     def __str__(self):
#         return str(self.current_user)


class Prompt(models.Model):
    date = models.DateField()
    text = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.text


class Sketch(models.Model):
    sketch_data = models.JSONField()
    date = models.DateField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sketches', null=True)
    prompt = models.ForeignKey(
        Prompt, on_delete=models.CASCADE, related_name='sketches', null=True)
