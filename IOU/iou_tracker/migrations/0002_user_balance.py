# Generated by Django 4.0.6 on 2023-02-26 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iou_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='balance',
            field=models.FloatField(default=0),
        ),
    ]
