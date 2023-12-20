from django.db import models
from django.utils import timezone
from user.models import User


class Diary(models.Model):
    created_time = models.DateTimeField(
        default=timezone.now, editable=False, verbose_name="Günlüğün Oluşturulma Tarihi")
    user = models.ForeignKey(
        User, verbose_name="Günlüğün Ait Olduğu Kullanıcı", on_delete=models.CASCADE)
    baslik = models.CharField(max_length=300, verbose_name="Günlük Basligi")
    note = models.TextField(verbose_name="Günlük Açıklaması")

    def __str__(self):
        return f'  {self.baslik , self.user}'
