# Generated by Django 2.2.9 on 2020-01-21 06:27

import askcompany.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20200121_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='photo',
            field=models.ImageField(upload_to=askcompany.utils.uuid_upload_to),
        ),
    ]
