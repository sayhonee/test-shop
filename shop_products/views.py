import itertools

from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView

from shop_order.forms import UserNewOrderForm
from .forms import PostForm
from .models import Product, Gallery
from shop_tag.models import Tag
from shop_category.models import ProductCategory


# Create your views here.


class ProductsList(ListView):
    template_name = "products/products_list.html"
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.get_active_products()


class ProductsListByCategory(ListView):
    template_name = "products/products_list.html"
    paginate_by = 6

    def get_queryset(self):
        category_name = self.kwargs["category_name"]
        category = ProductCategory.objects.filter(name__iexact=category_name).first()
        if category is None:
            raise Http404("صفحه ی مورد نظر یافت نشد")
        return Product.objects.get_products_by_category(category_name)


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def product_detail(request, *args, **kwargs):
    product_id = kwargs["productid"]

    new_order_form = UserNewOrderForm(request.POST or None,initial={"product_id":product_id})

    product:Product = Product.objects.get_by_id(product_id)
    if product is None or not product.active:
        raise Http404

    product.visit_count +=1
    product.save()

    related_products = Product.objects.get_queryset().filter(categories__product=product).distinct()

    grouped_related_products = my_grouper(3, related_products)

    galleries = Gallery.objects.filter(product_id=product_id)
    grouped_galleries = list(my_grouper(3, galleries))

    # code behind the post form
    post_form = PostForm(request.POST or None)
    if post_form.is_valid():
        full_name = post_form.cleaned_data.get("name")
        email = post_form.cleaned_data.get("email")

        text = post_form.cleaned_data.get("body")
        PostForm.objects.create(full_name=full_name, email=email, text=text, )
        post_form.save()
        # todo : show user a success message
        post_form = PostForm

    context = {
        "product": product,
        "post_form": post_form,
        "galleries": grouped_galleries,
        "related_products": grouped_related_products,
        "new_order_form": new_order_form
    }

    tag = Tag.objects.first()
    print(tag.products.all())

    return render(request, "products/product_detail.html", context)


class SearchProductsView(ListView):
    template_name = "products/products_list.html"
    paginate_by = 6

    def get_queryset(self):
        request = self.request
        query = request.GET.get("q")
        if query is not None:
            return Product.objects.Searh(query)

        return Product.objects.get_active_products()


def products_category_partial(request):
    categories = ProductCategory.objects.all()
    context = {
        "categories": categories
    }
    return render(request, "products/products_categories_partial.html", context)
