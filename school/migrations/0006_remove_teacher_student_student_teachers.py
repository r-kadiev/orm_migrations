# Generated by Django 4.0.5 on 2022-07-03 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_remove_student_teacher_teacher_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='student',
        ),
        migrations.AddField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(related_name='students', to='school.teacher'),
        ),
    ]