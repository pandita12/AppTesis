# Generated by Django 4.0 on 2022-11-09 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0002_remove_evaluation_professor_remove_evaluation_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluation',
            name='contents',
        ),
    ]
