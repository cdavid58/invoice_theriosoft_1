# Generated by Django 3.2.8 on 2023-03-27 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documentI', models.CharField(max_length=10)),
                ('dv', models.CharField(max_length=1)),
                ('name', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('typeDocumentId', models.CharField(max_length=1)),
                ('typeOrganization', models.CharField(max_length=1)),
                ('municipality', models.CharField(max_length=4)),
                ('tpyeRegimen', models.CharField(max_length=1)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
    ]
