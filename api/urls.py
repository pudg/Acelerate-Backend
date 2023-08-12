from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("api/", views.api, name="api"),
    path("api/<str:platform>/restaurant/<int:identifier>/reviews", views.restaurant_reviews, name="reviews"),
    path("api/<str:platform>/restaurant/<int:identifier>/worst", views.restaurant_worst, name="worst"),
    path("api/<str:platform>/restaurant/<int:identifier>/best", views.restaurant_best, name="beset"),
]