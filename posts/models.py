from django.db import models


# Create Models for Post
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
