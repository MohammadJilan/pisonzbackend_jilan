# Generated by Django 5.1.3 on 2024-11-30 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_remove_myuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='username',
            field=models.CharField(default='Username', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
