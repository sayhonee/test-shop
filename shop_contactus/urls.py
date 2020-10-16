from django.urls import path
from .views import contactpage
urlpatterns = [
    path('contact-us', contactpage)


]