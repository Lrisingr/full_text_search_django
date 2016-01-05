# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-05 19:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            "CREATE INDEX items_item_name_ts_idx ON items_item USING gin(to_tsvector('english', name));"
            "DROP INDEX IF EXISTS items_item_name_ts_idx;"
        ),
        migrations.RunSQL(
            "CREATE INDEX items_part_name_ts_idx ON items_part USING gin(to_tsvector('english', name));"
            "DROP INDEX IF EXISTS items_part_name_ts_idx;"
        ),
    ]