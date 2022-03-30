from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appointments/', include(('appointment.urls', 'appointments'), namespace='appointments')),
    path('accounts/', include('allauth.urls')),
]
