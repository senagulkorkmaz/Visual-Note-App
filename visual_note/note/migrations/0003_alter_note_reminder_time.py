# Generated by Django 4.1.3 on 2023-12-20 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_note_folder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='reminder_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
