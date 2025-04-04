# Generated by Django 5.1.7 on 2025-03-19 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_rename_height_feeder_mesuredheight_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeder',
            name='mesuredHeight',
            field=models.CharField(blank=True, help_text='mesuredHeight in cm', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='feeder',
            name='stepCount',
            field=models.PositiveIntegerField(blank=True, help_text='Number of stepCount', null=True),
        ),
    ]
