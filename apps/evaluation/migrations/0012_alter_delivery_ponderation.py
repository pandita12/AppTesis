# Generated by Django 4.0 on 2022-12-28 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0011_delivery_ponderation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='ponderation',
            field=models.FloatField(max_length=10, null=True),
        ),
    ]