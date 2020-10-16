import os

from django.db import models


# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"

    return f"sliders/{final_name}"


class Sliders(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان")
    re_title = models.CharField(max_length=150, verbose_name="عنوان2")
    link = models.URLField(max_length=150, verbose_name="آدرس")
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name="عکس")
    description = models.TextField(verbose_name="توضیحات")

    class Meta:
        verbose_name = "اسلایدر"
        verbose_name_plural = "اسلایدرها"

    def __str__(self):
        return self.title