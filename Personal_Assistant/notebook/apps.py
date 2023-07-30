from django.apps import AppConfig


class NotebookConfig(AppConfig):
    """
    Configuration class for the 'notebook' app.

    Attributes:
        default_auto_field (str): The default primary key field for models.
        name (str): The name of the app.
    """

    default_auto_field: str = "django.db.models.BigAutoField"
    name: str = "notebook"
