# Generated by Django 5.1.2 on 2024-11-02 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_uploadmodel_alter_course_isupdated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='imageUrl',
        ),
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
