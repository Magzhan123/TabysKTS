# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='main_image',
            field=models.CharField(max_length=512, null=True),
            preserve_default=True,
        ),
    ]
