# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2020-11-27 05:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pruebaEvertec.user_profiles.models.models
import pruebaEvertec.utils.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_photo', models.ImageField(storage=pruebaEvertec.utils.storage.OverwriteStorage(), upload_to=pruebaEvertec.user_profiles.models.models.get_cover_photo, verbose_name='cover photo')),
                ('marital_status', models.IntegerField(verbose_name='Marital Status')),
                ('siblings', models.BooleanField(verbose_name='Siblings')),
                ('birthday', models.DateField(verbose_name='Birthday')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name_plural': 'User Profiles',
            },
        ),
    ]
