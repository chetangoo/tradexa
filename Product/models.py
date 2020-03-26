from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model



class Product(models.Model):
    name = models.CharField(max_length = 30 , unique = True)
    weight = models.DecimalField(decimal_places= 2 , max_digits = 30)
    price = models.BigIntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        app_label = 'Product'
