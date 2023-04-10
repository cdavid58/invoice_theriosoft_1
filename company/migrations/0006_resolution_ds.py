# Generated by Django 3.2.8 on 2023-04-01 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_consecutive'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resolution_DS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('from_date', models.CharField(max_length=12)),
                ('to_date', models.CharField(max_length=12)),
                ('prefix', models.CharField(blank=True, max_length=7, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
    ]
