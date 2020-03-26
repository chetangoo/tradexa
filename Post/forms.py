from django import forms
from . import models


class PostForm(forms.ModelForm):
    class Meta:
        fields = ("text", "user")
        model = models.Post
