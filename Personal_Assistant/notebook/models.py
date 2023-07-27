from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'user'], name='user tags')
        ]

class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='notes', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def get_absolute_url(self):
        return reverse('note', kwargs={'note_id': self.pk})
    