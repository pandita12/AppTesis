# Generated by Django 4.0 on 2022-05-25 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0006_alter_user_first_name_alter_user_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.SlugField(max_length=255),
        ),
    ]