# Generated by Django 3.1.5 on 2024-04-06 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0012_bug_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventstare',
            name='descriere',
        ),
        migrations.RemoveField(
            model_name='eventstare',
            name='stare_noua',
        ),
        migrations.RemoveField(
            model_name='eventstare',
            name='stare_veche',
        ),
        migrations.AddField(
            model_name='eventstare',
            name='status_code',
            field=models.IntegerField(null=True),
        ),
    ]
