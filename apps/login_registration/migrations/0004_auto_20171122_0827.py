# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 16:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_registration', '0003_auto_20171122_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='login_registration.User'),
        ),
        migrations.AlterField(
            model_name='answercomment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answercomments', to='login_registration.User'),
        ),
        migrations.AlterField(
            model_name='questioncomment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questioncomments', to='login_registration.User'),
        ),
    ]