# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-13 14:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BooksReviewApp', '0005_auto_20180113_1645'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='author',
            new_name='author_pk',
        ),
    ]
