# Generated by Django 4.0 on 2023-01-20 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0026_delivery_title_task_alter_observation_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='evaluation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='evaluation', to='evaluation.evaluation'),
        ),
    ]
