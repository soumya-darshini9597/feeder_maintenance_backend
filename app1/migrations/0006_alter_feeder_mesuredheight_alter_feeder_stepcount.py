# Generated by Django 5.1.7 on 2025-03-19 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_feeder_mesuredheight_alter_feeder_stepcount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeder',
            name='mesuredHeight',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='feeder',
            name='stepCount',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
