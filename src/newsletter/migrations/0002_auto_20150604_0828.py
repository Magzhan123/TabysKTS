# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='update',
            new_name='updated',
        ),
        migrations.AlterField(
            model_name='signup',
            name='full_name',
            field=models.CharField(default=b'', max_length=120, null=True),
        ),
    ]
