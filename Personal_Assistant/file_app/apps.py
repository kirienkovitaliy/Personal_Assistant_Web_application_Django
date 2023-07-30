from django.apps import AppConfig


class FileAppConfig(AppConfig):
    """
    AppConfig for the 'file_app' Django app.

    This class is responsible for configuring the 'file_app' app and specifying its default
    auto field and name.

    Attributes:
        default_auto_field (str): The default auto field to use for model primary keys.
        name (str): The name of the app ('file_app').
    """

    default_auto_field: str = "django.db.models.BigAutoField"
    name: str = "file_app"
