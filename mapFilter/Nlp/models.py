from django.contrib.auth.models import AbstractUser
from django.db import models

from django.urls import reverse

from mapFilter import settings


class MyUser(AbstractUser):
    paid_subscription = models.BooleanField(default=False)

class diary_entries(models.Model):
    text = models.TextField(verbose_name='Diary entry')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Time create')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Time update')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User')

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'User record'
        ordering = ['-time_create']
