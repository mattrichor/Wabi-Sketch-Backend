# Generated by Django 4.1 on 2022-09-02 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wabi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(null=True, related_name='friends', to='wabi.user'),
        ),
    ]
