# Generated by Django 3.2.3 on 2021-05-26 13:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('kie_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordering',
            name='title',
        ),
        migrations.AddField(
            model_name='ordering',
            name='title',
            field=models.CharField(default=datetime.datetime(2021, 5, 26, 13, 40, 21, 909384, tzinfo=utc), max_length=250, verbose_name='posts'),
            preserve_default=False,
        ),
    ]
