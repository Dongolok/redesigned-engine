# Generated by Django 3.0.4 on 2020-04-21 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(default=1234, max_length=1000),
        ),
    ]
