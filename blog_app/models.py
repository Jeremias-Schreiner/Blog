from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Post(models.Model):
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    #image = models.ImageField(upload_to='images/', blank=True, null=True) imagen vieja
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    post = models.ForeignKey(Post, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/') 

    def __str__(self):
        return f"http://127.0.0.1:8000{self.image.url}"