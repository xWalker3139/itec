# Generated by Django 3.1.5 on 2024-04-06 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0017_auto_20240407_0218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aplicatie',
            name='este_activa',
        ),
    ]