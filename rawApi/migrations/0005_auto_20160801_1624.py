# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rawApi', '0004_auto_20160801_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zip',
            name='city',
            field=models.ForeignKey(to='rawApi.City'),
        ),
        migrations.AlterField(
            model_name='zip',
            name='country',
            field=models.ForeignKey(to='rawApi.Country'),
        ),
        migrations.AlterField(
            model_name='zip',
            name='state',
            field=models.ForeignKey(to='rawApi.State'),
        ),
    ]
