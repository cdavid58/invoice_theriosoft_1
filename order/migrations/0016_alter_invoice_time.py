# Generated by Django 3.2.8 on 2023-04-01 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_auto_20230401_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='time',
            field=models.CharField(default='11:38:01', max_length=10),
        ),
    ]
