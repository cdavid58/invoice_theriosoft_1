# Generated by Django 3.2.8 on 2023-03-27 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_company_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='resolution_elec',
            name='prefix',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]
