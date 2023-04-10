# Generated by Django 3.2.8 on 2023-03-27 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_alter_invoice_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='discountP',
            field=models.IntegerField(blank=True, default=0, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='durationMeasure',
            field=models.IntegerField(default=0, max_length=2),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='ipo',
            field=models.IntegerField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='iva',
            field=models.IntegerField(max_length=2),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='number',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='paymentForm',
            field=models.IntegerField(max_length=1),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='paymentMethods',
            field=models.IntegerField(max_length=2),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='price',
            field=models.IntegerField(max_length=20),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='quanty',
            field=models.IntegerField(max_length=20),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='time',
            field=models.CharField(default='15:53:45', max_length=10),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='typeDocumentId',
            field=models.IntegerField(max_length=1),
        ),
    ]