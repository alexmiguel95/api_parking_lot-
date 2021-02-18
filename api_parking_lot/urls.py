from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('accounts.urls')),
    path('api/', include('levels.urls')),
    path('api/', include('pricings.urls')),
    path('api/', include('vehicles.urls')),
    path('admin/', admin.site.urls)
]
