# Generated by Django 4.0 on 2023-01-06 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0017_delivery_evaluative_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='evaluation_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluation', to='evaluation.evaluation'),
        ),
    ]
