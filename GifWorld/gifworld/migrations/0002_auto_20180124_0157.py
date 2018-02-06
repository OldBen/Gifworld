# Generated by Django 2.0 on 2018-01-24 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifworld', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='csgogif',
            name='weapon_used',
            field=models.CharField(choices=[('PI', 'Pistol'), ('RI', 'Rifle'), ('SR', 'Sniper'), ('GR', 'Grenade'), ('OT', 'Other')], default='PI', max_length=2),
        ),
        migrations.AddField(
            model_name='owgif',
            name='hero_class',
            field=models.CharField(choices=[('OF', 'Offense'), ('DE', 'Defense'), ('TA', 'Tank'), ('SU', 'Support')], default='OF', max_length=2),
        ),
        migrations.AlterField(
            model_name='csgogif',
            name='image',
            field=models.ImageField(upload_to='static/gifworld/csgo'),
        ),
        migrations.AlterField(
            model_name='owgif',
            name='image',
            field=models.ImageField(upload_to='static/gifworld/ow'),
        ),
    ]