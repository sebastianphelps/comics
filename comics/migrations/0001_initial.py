# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import comics.models
import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('blurb', models.TextField(null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=comics.models.upload_path_and_rename, blank=True)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('post_type', models.CharField(max_length=32, choices=[(b'COMIC', b'Comic'), (b'THOUGHT', b'Thought')])),
                ('num_likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PostStyle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('border_colour', colorfield.fields.ColorField(max_length=10)),
                ('text_colour', colorfield.fields.ColorField(max_length=10)),
                ('background_colour', colorfield.fields.ColorField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='style',
            field=models.ForeignKey(blank=True, to='comics.PostStyle', null=True),
        ),
    ]
