# Generated by Django 4.0 on 2022-11-20 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0005_rename_fecha_nc_evaluation_date_finish_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='support_material',
            field=models.FileField(null=True, upload_to='material'),
        ),
    ]
