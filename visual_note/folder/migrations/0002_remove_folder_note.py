# Generated by Django 4.1.3 on 2023-12-20 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('folder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='note',
        ),
    ]
