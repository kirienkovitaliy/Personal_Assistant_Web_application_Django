from django.apps import AppConfig


class ExchangeRateConfig(AppConfig):
    """
    Configuration class for the "exchange_rate" app.
    Used for setting up the app and registering it in the Django project.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "exchange_rate"
