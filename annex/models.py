from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField("Аватар", upload_to="annex/img/%Y/%m/%d", default='annex/img/avatar_big.png', null=True)
    class Meta:
      verbose_name = "Сотрудники"
      verbose_name_plural = "Сотрудники"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Company(models.Model):
    name = models.CharField("Название компании", max_length = 80)
    city = models.CharField("Город", max_length = 80)
    background = models.ImageField("Фон", upload_to="annex/img/%Y/%m/%d", default='')

    def __str__(self):
        return self.name
        return self.city

    class Meta:
      verbose_name = "Все компании"
      verbose_name_plural = "Все компании"
