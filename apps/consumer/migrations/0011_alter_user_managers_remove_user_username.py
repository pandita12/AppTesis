# Generated by Django 4.0 on 2022-12-27 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0010_user_username'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
