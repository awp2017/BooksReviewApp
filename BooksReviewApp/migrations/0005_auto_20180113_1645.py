# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-13 14:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BooksReviewApp', '0004_review_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='author_pk',
            new_name='author',
        ),
    ]
