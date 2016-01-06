# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-06 13:04
from __future__ import unicode_literals

from django.db import migrations



class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            'CREATE FULLTEXT INDEX items_item_name_ts_idx ON items_item(name);',
            'ALTER TABLE items_item DROP INDEX items_item_name_ts_idx;',
        ),
        migrations.RunSQL(
            'CREATE FULLTEXT INDEX items_part_name_ts_idx ON items_part(name);',
            'ALTER TABLE items_part DROP INDEX items_part_name_ts_idx;',
        )
    ]