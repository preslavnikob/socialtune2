# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-20 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialtune', '0010_locations'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='insta_followed_by',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='users',
            name='insta_follows',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='users',
            name='insta_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='users',
            name='insta_media_count',
            field=models.IntegerField(default=0),
        ),
    ]
