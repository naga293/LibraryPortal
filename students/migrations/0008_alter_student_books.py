# Generated by Django 4.1.1 on 2022-09-07 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_alter_student_no_of_pages_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='books',
            field=models.ManyToManyField(blank=True, default=None, to='students.book'),
        ),
    ]
