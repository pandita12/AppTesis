# Generated by Django 4.0 on 2022-11-10 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0003_remove_evaluation_contents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='support_material',
            field=models.FileField(upload_to='material'),
        ),
    ]
