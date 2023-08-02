from django.contrib.auth.models import User
from django.db import models


class File(models.Model):
    """
    Model representing a file uploaded by a user.

    Attributes:
        name (models.CharField): The name of the file.
        file (models.FileField): The file field for storing the file itself.
        user (models.ForeignKey): The foreign key to the User model representing the user who uploaded the file.
        category (models.CharField): The category of the file.
        created_at (models.DateTimeField): The timestamp when the file was created.
    """

    name: models.CharField = models.CharField(max_length=255)
    file: models.FileField = models.FileField()
    user: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)
    category: models.CharField = models.CharField(max_length=100)
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    def delete(self):
        """
        Override the delete method to also delete the associated file from the storage.

        This method deletes the file from the storage using the `file.delete()` method
        before deleting the object from the database using the `super().delete()` method.
        """
        self.file.delete()
        super().delete()
