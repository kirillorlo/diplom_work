# Generated by Django 5.0.6 on 2024-06-18 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_client_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='user',
        ),
        migrations.AddField(
            model_name='client',
            name='password',
            field=models.CharField(default=None, max_length=15),
            preserve_default=False,
        ),
    ]
