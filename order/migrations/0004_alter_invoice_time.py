# Generated by Django 3.2.8 on 2023-03-27 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_invoice_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='time',
            field=models.CharField(default='15:26:07', max_length=10),
        ),
    ]