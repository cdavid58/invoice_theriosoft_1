# Generated by Django 3.2.8 on 2023-04-01 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0018_alter_invoice_time'),
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.invoice'),
        ),
    ]
