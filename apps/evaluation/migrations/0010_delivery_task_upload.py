# Generated by Django 4.0 on 2022-12-09 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0009_config_delivery_rest_delivery_status_delivery_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='task_upload',
            field=models.FileField(blank=True, null=True, upload_to='taskupload/'),
        ),
    ]
