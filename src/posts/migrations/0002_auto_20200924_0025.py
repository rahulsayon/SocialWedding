# Generated by Django 3.0.7 on 2020-09-23 18:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20200923_2339'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='posts', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
        migrations.AlterField(
            model_name='post',
            name='liked',
            field=models.ManyToManyField(blank=True, related_name='likes', to='profiles.Profile'),
        ),
    ]
