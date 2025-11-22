"""Models for the `core` application.

Includes a custom User model, a demo CustomModel with JSON data,
and a RelatedItem model used as an inline example in the admin.
"""

from typing import Any, Dict

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.validators import MinLengthValidator

from .fields import UpperCaseCharField, PhoneNumberField


class User(AbstractUser):
    """Custom user extending Django's AbstractUser.

    Adds an optional `phone_number` field.
    """
    phone_number = PhoneNumberField(blank=True, null=True)

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.username


class CustomModel(models.Model):
    """A demo model to show custom fields and JSON storage.

    Methods:
        stats: return simple statistics about description and JSON data.
    """
    title = UpperCaseCharField(max_length=200)
    description = models.TextField(blank=True)
    data = models.JSONField(default=dict, blank=True)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Custom Model'
        verbose_name_plural = 'Custom Models'

    def __str__(self) -> str:
        return self.title

    def stats(self) -> Dict[str, int]:
        """Return basic statistics for the object.

        Returns a mapping containing the number of words in the
        description and the number of keys in the JSON `data`.
        """
        words = len(self.description.split()) if self.description else 0
        keys = len(self.data.keys()) if isinstance(self.data, dict) else 0
        return {'words': words, 'json_keys': keys}


class RelatedItem(models.Model):
    """Simple item related to `CustomModel` for inline admin examples."""

    parent = models.ForeignKey(
        CustomModel, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, validators=[MinLengthValidator(1)])
    value = models.CharField(max_length=200, blank=True)

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"{self.parent.title} - {self.name}"
