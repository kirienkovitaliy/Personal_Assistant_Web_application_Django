import os
from uuid import uuid4
from django.contrib.auth.models import User
from django.db import models


def update_filename(instance: "Picture", filename: str) -> str:
    """
    Function to update the filename of an uploaded picture.

    This function generates a unique filename using a UUID and maintains the file extension.

    Args:
        instance (Picture): The instance of the Picture model.
        filename (str): The original filename of the uploaded picture.

    Returns:
        str: The updated filename with a unique identifier.
    """
    upload_to = f"uploads"
    ext = filename.split(".")[-1]
    filename = f"{uuid4().hex}.{ext}"
    return os.path.join(upload_to, filename)


class Picture(models.Model):
    """
    Model to store pictures uploaded by users.

    This model represents pictures uploaded by users. Each picture has a description,
    a file path, and is associated with a user through a foreign key relationship.

    Attributes:
        description (models.CharField): A field to store the description of the picture.
            It has a maximum length of 150 characters.
        path (models.FileField): A field to store the file path of the uploaded picture.
            The 'upload_to' attribute is set to the 'update_filename' function, which generates
            a unique filename for each uploaded picture.
        user (models.ForeignKey): A foreign key relationship to the User model.
            It represents the user who uploaded the picture. It is optional and can be null or blank.
    """

    description = models.CharField(max_length=150)
    path = models.FileField(upload_to=update_filename)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, null=True, blank=True
    )

    def __str__(self) -> str:
        """
        Returns a string representation of the Picture model.

        This method returns a string containing the username and email of the user who uploaded
        the picture, along with the picture's file path.

        Returns:
            str: String representation of the Picture model.
        """
        return f"{self.user.username}({self.user.email}): {self.path}"
