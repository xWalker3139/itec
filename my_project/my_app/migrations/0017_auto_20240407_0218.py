# Generated by Django 3.1.5 on 2024-04-06 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0016_auto_20240407_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='stare',
            field=models.CharField(default='Unknown', max_length=256, null=True),
        ),
    ]
