# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Image', models.ImageField(upload_to=b'images/')),
                ('Filters', models.CharField(default=b'BLUR', max_length=100, choices=[(b'BLUR', b'BLUR'), (b'CONTOUR', b'CONTOUR'), (b'DETAIL', b'DETAIL'), (b'EDGE_ENHANCE', b'EDGE_ENHANCE')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
