# Generated by Django 4.0 on 2023-01-04 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0012_alter_delivery_ponderation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery_rest',
            name='is_approved',
        ),
        migrations.RemoveField(
            model_name='delivery_rest',
            name='is_reprobate',
        ),
        migrations.AddField(
            model_name='delivery_rest',
            name='claim',
            field=models.CharField(max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='delivery_rest',
            name='observation',
            field=models.CharField(choices=[('N', 'Still to deliver'), ('I', 'Incomplete content')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='ponderation',
            field=models.FloatField(null=True),
        ),
    ]
