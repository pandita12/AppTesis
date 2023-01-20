# Generated by Django 4.0 on 2023-01-20 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0025_rename_user_delivery_student_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='title_task',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='observation',
            name='delivery',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='observation_delivery', to='evaluation.delivery'),
        ),
    ]
