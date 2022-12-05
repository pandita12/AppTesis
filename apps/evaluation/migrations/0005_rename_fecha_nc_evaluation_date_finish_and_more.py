# Generated by Django 4.0 on 2022-11-15 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0005_remove_professor_category'),
        ('evaluation', '0004_alter_evaluation_support_material'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evaluation',
            old_name='fecha_nc',
            new_name='date_finish',
        ),
        migrations.AddField(
            model_name='evaluation',
            name='date_start',
            field=models.DateTimeField(),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='classroom_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluation', to='lesson.classroom'),
        ),
    ]