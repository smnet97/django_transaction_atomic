from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
                  path("admin/", admin.site.urls),
                  path('', include('product.urls')),
                  path('', include('order.urls')),
                  path('', include('user.urls')),
                  path('', include('book.urls')),
                  path('', include('django_prometheus.urls')),
              ] + debug_toolbar_urls()
