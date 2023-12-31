# Generated by Django 4.1.3 on 2023-12-20 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='To_Do_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Yapılacak Notun Oluşturulma Tarihi')),
                ('baslik', models.CharField(max_length=300, verbose_name='Yapılacak Not Basligi')),
                ('note', models.TextField(verbose_name='Yapılacak Not Açıklaması')),
                ('reminder_time', models.DateTimeField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False, verbose_name='Tamamlandı mı?')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yapılacak Notun Ait Olduğu Kullanıcı')),
            ],
        ),
    ]
