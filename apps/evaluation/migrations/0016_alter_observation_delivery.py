# Generated by Django 4.0 on 2023-01-05 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0015_alter_observation_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observation',
            name='delivery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='observation_delivery', to='evaluation.delivery'),
        ),
    ]
