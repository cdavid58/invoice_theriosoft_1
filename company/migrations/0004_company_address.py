# Generated by Django 3.2.8 on 2023-03-27 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_resolution_elec_prefix'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]