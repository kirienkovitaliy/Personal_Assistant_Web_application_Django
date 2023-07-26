from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'user'], name='user tags')
        ]

class Note(models.Mpdel):
    head = models.CharField(max_length=255)
    body = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='notes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    