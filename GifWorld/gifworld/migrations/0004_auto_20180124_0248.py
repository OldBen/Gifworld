# Generated by Django 2.0 on 2018-01-24 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifworld', '0003_auto_20180124_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csgogif',
            name='image',
            field=models.ImageField(max_length=255, upload_to='upload/csgo'),
        ),
        migrations.AlterField(
            model_name='owgif',
            name='image',
            field=models.ImageField(max_length=255, upload_to='upload/ow'),
        ),
    ]
