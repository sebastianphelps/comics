# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poststyle',
            name='id',
        ),
        migrations.AlterField(
            model_name='poststyle',
            name='name',
            field=models.CharField(max_length=255, unique=True, serialize=False, primary_key=True),
        ),
    ]
