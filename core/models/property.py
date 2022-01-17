from django.db import models

from .base_model import BaseModel


def limits_info():
    return []


class Property(BaseModel):
    name = models.CharField(max_length=500)
    full_limits = models.JSONField("limitsInfo", default=limits_info)

    def __str__(self):
        return f'{self.name}'
