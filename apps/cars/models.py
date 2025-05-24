from django.db import models

from apps.users.models import CustomUser
from utils.base_model import BaseModel


class Car(BaseModel):
    name = models.CharField(max_length=60)
    year = models.PositiveIntegerField()
    description = models.TextField()
    sold = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.year})"
