# Generated by Django 3.0.4 on 2020-05-07 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0006_auto_20200429_1229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='check',
            name='totalsum',
        ),
    ]
