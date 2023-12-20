from django.db import models
from django.utils import timezone
from user.models import User


class To_Do_List(models.Model):
    created_time = models.DateTimeField(
        default=timezone.now, editable=False, verbose_name="Yapılacak Notun Oluşturulma Tarihi")
    user = models.ForeignKey(
        User, verbose_name="Yapılacak Notun Ait Olduğu Kullanıcı", on_delete=models.CASCADE)
    baslik = models.CharField(
        max_length=300, verbose_name="Yapılacak Not Basligi")
    note = models.TextField(verbose_name="Yapılacak Not Açıklaması")
    reminder_time = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(
        default=False, verbose_name="Tamamlandı mı?")

    def __str__(self):
        return f'  {self.baslik , self.user}'
