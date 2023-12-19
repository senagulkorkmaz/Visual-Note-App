from django.db import models
from django.contrib.auth.models import AbstractUser
from visual_note.utils import get_upload_path


class User(AbstractUser, models.Model):
    onay_bekleniyor = ("onay_bekleniyor")
    onaylandi = ("onaylandi")
    reddedildi = ("reddedildi")
    image_durumu = (
        (onay_bekleniyor, onay_bekleniyor), (onaylandi,
                                             onaylandi), (reddedildi, reddedildi)
    )

    email = models.EmailField('Email', max_length=255,
                              unique=True, blank=True, null=True)
    password = models.CharField(max_length=100)
    old_password = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(
        verbose_name="Name", max_length=128, blank=True, null=True)
    last_name = models.CharField(
        verbose_name="Surname", max_length=128, blank=True, null=True)
    username = models.CharField(
        verbose_name="Username", max_length=128, unique=True)

    image = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    image_status = models.CharField(choices=image_durumu, default=None,
                                    verbose_name='İmage Durumu', max_length=100, blank=True, null=True)

    access_token = models.CharField(max_length=200, blank=True, null=True)
    refresh_token = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.pk}'
