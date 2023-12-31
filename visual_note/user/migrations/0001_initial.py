# Generated by Django 4.1.3 on 2023-12-19 12:38

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone
import visual_note.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='Email')),
                ('password', models.CharField(max_length=100)),
                ('old_password', models.CharField(blank=True, max_length=100, null=True)),
                ('first_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='Name')),
                ('last_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='Surname')),
                ('username', models.CharField(max_length=128, unique=True, verbose_name='Username')),
                ('image', models.ImageField(blank=True, null=True, upload_to=visual_note.utils.get_upload_path)),
                ('image_status', models.CharField(blank=True, choices=[('onay_bekleniyor', 'onay_bekleniyor'), ('onaylandi', 'onaylandi'), ('reddedildi', 'reddedildi')], default=None, max_length=100, null=True, verbose_name='İmage Durumu')),
                ('access_token', models.CharField(blank=True, max_length=200, null=True)),
                ('refresh_token', models.CharField(blank=True, max_length=200, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
