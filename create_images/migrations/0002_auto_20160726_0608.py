# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('create_images', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='Filters',
            new_name='Filter',
        ),
    ]
