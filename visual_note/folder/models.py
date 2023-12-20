from django.db import models
from django.utils import timezone
from user.models import User


class Folder(models.Model):
    created_time = models.DateTimeField(
        default=timezone.now, editable=False, verbose_name="Klasör Oluşturulma Tarihi")
    user = models.ForeignKey(
        User, verbose_name="Klasörün Ait Olduğu Kullanıcı", on_delete=models.CASCADE)

    baslik = models.CharField(max_length=300, verbose_name="Klasör Basligi")

    def __str__(self):
        return f'  {self.pk , self.user}'
