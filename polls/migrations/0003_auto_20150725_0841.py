# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_question_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_creator',
            field=models.CharField(max_length=100),
        ),
    ]
