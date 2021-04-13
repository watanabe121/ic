from django.contrib import admin
from django.urls import path, include
from icorder import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('icorder.urls')),
]
