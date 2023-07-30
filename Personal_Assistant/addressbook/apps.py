from django.apps import AppConfig


class AddressbookConfig(AppConfig):
    """
    AppConfig class for the "addressbook" app.

    Attributes:
        default_auto_field (str): The default primary key field for models in this app.
        name (str): The name of the app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "addressbook"
