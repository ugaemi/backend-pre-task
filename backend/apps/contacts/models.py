from django.db import models


class ContactLabel(models.Model):
    """
    연락처 라벨 모델
    """
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name='contact_labels')
    name = models.CharField(max_length=30, verbose_name="이름")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일시")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일시")


class Contact(models.Model):
    """
    연락처 모델
    """
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=30, verbose_name="이름")
    email = models.EmailField(verbose_name="이메일", null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="전화번호")
    company = models.CharField(max_length=30, null=True, blank=True, verbose_name="회사")
    position = models.CharField(max_length=30, null=True, blank=True, verbose_name="직책")
    memo = models.TextField(null=True, blank=True, verbose_name="메모")
    labels = models.ManyToManyField("contacts.ContactLabel", related_name='contacts', blank=True, verbose_name="라벨")
    profile_image_url = models.URLField(null=True, blank=True, verbose_name="프로필 사진")
    address = models.CharField(max_length=100, null=True, blank=True, verbose_name="주소")
    birthday = models.DateField(null=True, blank=True, verbose_name="생일")
    website = models.URLField(null=True, blank=True, verbose_name="웹사이트")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일시")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일시")
