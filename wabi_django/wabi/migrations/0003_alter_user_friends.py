# Generated by Django 4.1 on 2022-09-02 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wabi', '0002_alter_user_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='friends', to='wabi.user'),
        ),
    ]
