# Generated by Django 3.2.8 on 2023-03-27 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_invoice_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='time',
            field=models.CharField(default='15:20:27', max_length=10),
        ),
    ]
