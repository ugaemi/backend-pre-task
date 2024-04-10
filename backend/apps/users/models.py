from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    사용자 모델
    """
    email = models.EmailField(unique=True, db_index=True, verbose_name="이메일")
    password = models.CharField(max_length=128, verbose_name="비밀번호")
    name = models.CharField(max_length=30, verbose_name="이름")
    is_active = models.BooleanField(default=True, verbose_name="활성화 여부")
    is_staff = models.BooleanField(default=False, verbose_name="스태프 여부")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일시")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일시")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return self.email
