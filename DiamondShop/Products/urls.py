from django.urls import path
from . import views

urlpatterns = [
    path("category/", views.category_view, name='category'),
    path("detail/", views.detail_view, name='detail'),
    path("collection/", views.collection_view, name='collection'),
]