from django.db import models
from django.utils import timezone
from visual_note.utils import get_upload_path
from user.models import User


class Planner(models.Model):
    created_time = models.DateTimeField(
        default=timezone.now, editable=False, verbose_name="Günlüğün Oluşturulma Tarihi")
    user = models.ForeignKey(
        User, verbose_name="Günlüğün Ait Olduğu Kullanıcı", on_delete=models.CASCADE)
    baslik = models.CharField(max_length=300, verbose_name="Günlük Basligi")
    note = models.TextField(verbose_name="Günlük Açıklaması")
    image = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    reminder_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'  {self.baslik , self.user}'
