# Generated by Django 4.2.16 on 2024-11-24 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('region_app', '0003_cooperative_mission_cooperative_vesion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='system',
            name='fail_type',
            field=models.ManyToManyField(null=True, to='region_app.fail_type'),
        ),
    ]