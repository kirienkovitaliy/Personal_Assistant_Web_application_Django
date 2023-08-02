from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Tag(models.Model):
    """
    Model representing a Tag.

    Attributes:
        name (str): The name of the tag.
        user (ForeignKey): The user who created the tag.
    """

    name: str = models.CharField(max_length=100)
    user: models.ForeignKey = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["name", "user"], name="user tags")
        ]

    def __str__(self):
        """
        Return a string representation of the tag.
        """
        return f"{self.name}"


class Note(models.Model):
    """
    Model representing a Note.

    Attributes:
        title (str): The title of the note.
        content (str): The content of the note.
        tags (ManyToManyField): The tags associated with the note.
        user (ForeignKey): The user who created the note.
    """

    title: str = models.CharField(max_length=255)
    content: str = models.TextField(null=True, blank=True)
    tags: models.ManyToManyField = models.ManyToManyField(
        Tag, related_name="notes", blank=True
    )
    user: models.ForeignKey = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1
    )

    def get_absolute_url(self):
        """
        Get the URL for accessing the detail view of the note.
        """
        return reverse("notebook:note_detail", kwargs={"pk": self.pk})
