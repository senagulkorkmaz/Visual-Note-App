from django.db import models
from django.utils import timezone
from user.models import User
from visual_note.utils import get_upload_path
from folder.models import Folder


class Note(models.Model):
    created_time = models.DateTimeField(
        default=timezone.now, editable=False, verbose_name="Not Oluşturulma Tarihi")
    user = models.ForeignKey(
        User, verbose_name="Notun Ait Olduğu Kullanıcı", on_delete=models.CASCADE)
    folder = models.ForeignKey(
        Folder, verbose_name="Notun Ait Olduğu Klasör", on_delete=models.CASCADE, blank=True, null=True)
    baslik = models.CharField(max_length=300, verbose_name="Not Basligi")
    note = models.TextField(verbose_name="Not Açıklaması")
    image = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    reminding = models.BooleanField(
        default=False, verbose_name="Not Hatırlatmalı mı?")
    reminder_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'  {self.baslik , self.user}'
