# Generated by Django 3.2.8 on 2023-04-10 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0025_auto_20230410_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='time',
            field=models.CharField(default='09:57:48', max_length=10),
        ),
    ]