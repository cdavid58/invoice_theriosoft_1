# Generated by Django 3.2.8 on 2023-04-01 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_alter_invoice_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='time',
            field=models.CharField(default='12:02:45', max_length=10),
        ),
    ]
