# Generated by Django 5.0.6 on 2024-06-18 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_client_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='password',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
