# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='root',
            name='root',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterUniqueTogether(
            name='root',
            unique_together=set([('root', 'type')]),
        ),
    ]
