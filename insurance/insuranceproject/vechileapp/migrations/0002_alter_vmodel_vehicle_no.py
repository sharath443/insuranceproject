# Generated by Django 3.2.6 on 2021-08-20 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vechileapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vmodel',
            name='vehicle_no',
            field=models.SlugField(null=True),
        ),
    ]
