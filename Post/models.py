from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts",on_delete=models.CASCADE ,blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.text


    def get_absolute_url(self):
        return reverse(
            "posts:single",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["user",]
        app_label = 'Post'
