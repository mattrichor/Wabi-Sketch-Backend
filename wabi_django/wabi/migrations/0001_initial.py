# Generated by Django 4.1 on 2022-09-02 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prompt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=255, unique=True, verbose_name='email address')),
                ('username', models.CharField(max_length=100, null=True)),
                ('password', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=False)),
                ('friends', models.ManyToManyField(related_name='friends', to='wabi.user')),
            ],
        ),
        migrations.CreateModel(
            name='Sketch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sketch_data', models.JSONField()),
                ('date', models.DateField()),
                ('prompt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prompt', to='wabi.prompt')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='wabi.user')),
            ],
        ),
    ]
