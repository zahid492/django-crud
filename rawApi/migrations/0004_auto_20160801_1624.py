# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rawApi', '0003_auto_20160801_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='zip',
            name='city',
            field=models.ForeignKey(related_name='zip', default=b'', editable=False, to='rawApi.City'),
        ),
        migrations.AddField(
            model_name='zip',
            name='country',
            field=models.ForeignKey(related_name='zip', default=b'', editable=False, to='rawApi.Country'),
        ),
        migrations.AlterField(
            model_name='zip',
            name='state',
            field=models.ForeignKey(default=b'', editable=False, to='rawApi.State'),
        ),
    ]
