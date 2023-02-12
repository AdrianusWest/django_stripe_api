from django.apps import AppConfig


class PaymentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stripe_api_payment.payments'
    verbose_name = 'Оплата'
