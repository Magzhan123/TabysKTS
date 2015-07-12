# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('short_desc', models.TextField()),
                ('full_desc', models.TextField()),
                ('category', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('main_image', models.CharField(max_length=512)),
                ('added', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
            bases=(models.Model,),
        ),
    ]
