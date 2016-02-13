# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-13 15:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wallet', '0003_auto_20160206_0645'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transactions',
            options={'ordering': ('-created_at',), 'verbose_name': 'Transaction', 'verbose_name_plural': 'Transaction'},
        ),
        migrations.AddField(
            model_name='transactions',
            name='owner',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
