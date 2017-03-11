from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    PUBLISHED = "PUB"
    DRAFT = "DFT"
    STATUSES = (
        (PUBLISHED, "Published"),
        (DRAFT, "Draft")
    )

    title = models.CharField(max_length=60)
    author = models.ForeignKey(User, related_name="authored_posts")
    description = models.CharField(max_length=250, blank=True)
    content = models.TextField(blank=True)
    status = models.CharField(max_length=3, default=DRAFT, choices=STATUSES)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title