from django.db import models
from django.utils import timezone
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    post_slug = models.CharField(max_length=80, default="default_post")
    img = models.ImageField(default="blog/static/img/default.png", 
                            upload_to="blog/static/img", height_field=None,
                            width_field=None, max_length=200, 
                            verbose_name="Картинка для поста")

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.img.path)

        if img.height > 720 or img.width > 1080:
            img.thumbnail((720, 1080))
            img.save(self.img.path)
        
    def __str__(self):
        return self.title
