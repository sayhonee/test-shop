import itertools

from django.shortcuts import render

from shop_products.models import Product
from shop_sliders.models import Sliders
from shop_side_settings.models import SiteSetting
from shop_products.forms import PostForm


def header(request, *args, **kwargs):
    sidesetting = SiteSetting.objects.first()

    context = {
        "settings": sidesetting
    }
    return render(request, 'shared/Header.html', context)


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def homepage(request):
    sliders = Sliders.objects.all()
    most_visit_products = Product.objects.order_by("-visit_count").all()[:8]
    latest_products = Product.objects.order_by("-id").all()[:8]
    context = {
        "sliders": sliders,
        "most_visit":my_grouper(4,most_visit_products),
        "latest_products":my_grouper(4,latest_products)

    }
    return render(request, "home.html", context)


def footer(request):
    sidesetting = SiteSetting.objects.first()

    context = {
        "settings": sidesetting
    }
    return render(request, "shared/Footre.html", context)


def about_us(request):
    sidesetting = SiteSetting.objects.first()

    context = {
        "settings": sidesetting
    }
    return render(request, "shared/about_page.html", context)


def news_page(request):
    sidesetting = SiteSetting.objects.first()
    post_form = PostForm(request.POST or None)
    if post_form.is_valid():
        full_name = post_form.cleaned_data.get("name")
        email = post_form.cleaned_data.get("email")

        text = post_form.cleaned_data.get("body")
        PostForm.objects.create(full_name=full_name, email=email, text=text, )
        post_form.save()
        # todo : show user a success message

    context = {
        "settings": sidesetting,
        "post_form": post_form

    }
    return render(request, "shared/news_page.html", context)
