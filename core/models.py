from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.validators import MinLengthValidator
from .fields import UpperCaseCharField, PhoneNumberField


class User(AbstractUser):
    phone_number = PhoneNumberField(blank=True, null=True)

    def __str__(self):
        return self.username


class CustomModel(models.Model):
    title = UpperCaseCharField(max_length=200)
    description = models.TextField(blank=True)
    data = models.JSONField(default=dict, blank=True)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Custom Model'
        verbose_name_plural = 'Custom Models'

    def __str__(self):
        return self.title

    def stats(self):
        """Return simple statistics about `description` and `data`."""
        words = len(self.description.split()) if self.description else 0
        keys = len(self.data.keys()) if isinstance(self.data, dict) else 0
        return {'words': words, 'json_keys': keys}


class RelatedItem(models.Model):
    parent = models.ForeignKey(
        CustomModel, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, validators=[MinLengthValidator(1)])
    value = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.parent.title} - {self.name}"
