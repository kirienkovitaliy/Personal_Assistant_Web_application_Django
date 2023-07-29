from django.contrib.auth.models import User
from django.db import models


class File(models.Model):
    name = models.CharField()
    file = models.FileField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)

    def delete(self):
        self.file.delete()
        super().delete()
