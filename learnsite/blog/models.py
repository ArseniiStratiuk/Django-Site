from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    post_slug = models.CharField(max_length=80, default="default_post")
    
    
    def __str__(self):
        return self.title