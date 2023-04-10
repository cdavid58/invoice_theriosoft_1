# Generated by Django 3.2.8 on 2023-04-04 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0001_initial'),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='municipality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='setting.municipality'),
        ),
        migrations.AlterField(
            model_name='client',
            name='tpyeRegimen',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='setting.type_regime'),
        ),
        migrations.AlterField(
            model_name='client',
            name='typeDocumentId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='setting.type_document_identification'),
        ),
        migrations.AlterField(
            model_name='client',
            name='typeOrganization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='setting.type_organization'),
        ),
    ]
