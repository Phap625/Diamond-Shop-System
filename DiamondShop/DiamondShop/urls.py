from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("Home.urls")),
    path("cart/", include("Cart.urls")),
    path("accounts/", include("Accounts.urls")),
    path("", include("Products.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)