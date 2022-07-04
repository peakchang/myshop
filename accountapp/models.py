from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

RATE_CHOICE = (('A', '마스터'), ('B', '관리자'), ('C', '우수회원'), ('D', '기본회원'), ('E', '일반회원'))


class User(AbstractUser):
    rate = models.CharField(choices=RATE_CHOICE, max_length=20, null=True, default='E')
    nickname = models.CharField(max_length=20, null=True, blank=True, default='')
    phone = models.CharField(max_length=20, null=True, blank=True, default='')
    add_zip = models.CharField(max_length=100, null=True, blank=True, default='')
    add_info = models.CharField(max_length=100, null=True, blank=True, default='')
    add_detail = models.CharField(max_length=100, null=True, blank=True, default='')
    point = models.IntegerField(null=True, blank=True, default=0)
