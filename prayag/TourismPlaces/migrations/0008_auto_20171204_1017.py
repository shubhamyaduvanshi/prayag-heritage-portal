# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 10:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TourismPlaces', '0007_auto_20171204_0258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourismplace',
            name='image',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]