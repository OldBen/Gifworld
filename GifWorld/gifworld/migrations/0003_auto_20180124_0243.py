# Generated by Django 2.0 on 2018-01-24 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifworld', '0002_auto_20180124_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gif',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='gif',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
