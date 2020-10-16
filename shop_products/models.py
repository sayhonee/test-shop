from django.db.models import Q
from django.db import models
import os

# Create your models here.
from shop_category.models import ProductCategory


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"

    return f"products/{final_name}"


def upload_galleries_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"

    return f"products/galleries/{final_name}"


class ProductManager(models.Manager):
    def get_active_products(self):
        return self.get_queryset().filter(active=True)

    def get_products_by_category(self, category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name, active=True)

    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(id=product_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None


def Searh(self, query):
    lookup = (
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(tag__title__icontains=query)
    )

    return self.get_queryset().filter(lookup, active=True).distinct()


class Product(models.Model):
    title = models.CharField(max_length=120, verbose_name="عنوان")
    description = models.TextField(max_length=10000, verbose_name="توضیحات")
    short_desc = models.CharField(max_length=50, verbose_name="توضیح کوتاه")
    price = models.IntegerField(verbose_name="قیمت")
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name="عکس")
    active = models.BooleanField(default=False, verbose_name="فعال/غیر فعال")
    categories = models.ManyToManyField(ProductCategory, blank=True, verbose_name="دسته بندی ها")
    visit_count = models.IntegerField(default=0, verbose_name="تعداد بازدید")

    objects = ProductManager()

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/products/{self.id}/{self.title.replace('', '-')}"


class Comment(models.Model):
    post = models.ForeignKey(Product, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post} {self.name}"


class Gallery(models.Model):
    title = models.CharField(max_length=120, verbose_name="عنوان")
    image = models.ImageField(upload_to=upload_galleries_image_path, verbose_name="عکس")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "تصویر"
        verbose_name_plural = "گالری تصویر"

    def __str__(self):
        return self.title
