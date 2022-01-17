from django.contrib.auth.models import User
from django.db import models

from .base_model import BaseModel


class Location(BaseModel):
    houmer = models.ForeignKey(
        User,
        default=None,
        related_name='locations',
        on_delete=models.CASCADE,
    )
    latitude = models.DecimalField(
        max_digits=20,
        decimal_places=15,
        default=None
    )
    longitude = models.DecimalField(
        max_digits=20,
        decimal_places=15,
        default=None
    )

    def __str__(self):
        return f'{self.houmer}'
