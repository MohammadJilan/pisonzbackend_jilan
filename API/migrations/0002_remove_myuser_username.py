# Generated by Django 5.1.3 on 2024-11-30 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='username',
        ),
    ]