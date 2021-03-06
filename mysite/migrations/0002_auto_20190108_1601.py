# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-08 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='arecord_users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_name', models.CharField(max_length=200)),
                ('redirect_to_url', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=200)),
                ('permanent', models.CharField(max_length=200)),
                ('parameter_copy', models.CharField(max_length=200)),
                ('request_path', models.CharField(max_length=200)),
                ('domain_type', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('updated_date', models.CharField(max_length=200)),
                ('ssl_status', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='file_upload',
        ),
    ]
