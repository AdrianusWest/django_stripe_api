from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('stripe_api_payment.payments.urls')),
    path('admin/', admin.site.urls),
]
