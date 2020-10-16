from django.urls import path
from .views import ProductsList, product_detail, SearchProductsView, ProductsListByCategory,products_category_partial

urlpatterns = [

    path('products', ProductsList.as_view()),
    path('products/<productid>/<title>', product_detail),
    path('products/<category_name>', ProductsListByCategory.as_view()),
    path('products/search', SearchProductsView.as_view()),
    path('products_category_partial', products_category_partial,name="products_category_partial"),

]
