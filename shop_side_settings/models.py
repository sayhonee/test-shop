import os

from django.db import models


# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.title}{ext}"
    return f"logo-image/{final_name}"


class SiteSetting(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان سایت")
    address = models.CharField(max_length=400, verbose_name="آدرس ")
    phone = models.CharField(max_length=50, verbose_name="تلفن")
    mobile = models.CharField(max_length=50, verbose_name="تلفن همراه")
    fax = models.CharField(max_length=50, verbose_name="فکس")
    email = models.EmailField(max_length=150, verbose_name="ایمیل")
    about_us = models.TextField(verbose_name="در باره ی ما", null=True, blank=True)
    copy_right = models.CharField(max_length=90, verbose_name="متن کپی رایت", null=True, blank=True)
    logo_image = models.ImageField(verbose_name="تصویر لوگو", upload_to=upload_image_path, null=True, blank=True, )
    image_photo = models.ImageField(verbose_name="تصویر", upload_to=upload_image_path, null=True, blank=True, )

    class Meta:
        verbose_name = "تنظیمات سایت"
        verbose_name_plural = "مدیریت تنظیمات"

    def __str__(self):
        return self.title
