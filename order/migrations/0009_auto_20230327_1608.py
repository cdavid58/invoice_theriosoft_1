# Generated by Django 3.2.8 on 2023-03-27 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_auto_20230327_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='time',
            field=models.CharField(default='16:08:21', max_length=10),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='typeDocumentId',
            field=models.IntegerField(),
        ),
    ]
