# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rawApi', '0002_auto_20160801_0438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zip',
            name='city',
        ),
        migrations.RemoveField(
            model_name='zip',
            name='country',
        ),
        migrations.AlterField(
            model_name='zip',
            name='state',
            field=models.ForeignKey(related_name='Zip', to='rawApi.State'),
        ),
    ]
