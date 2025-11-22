"""Custom model fields used in the `core` app.

Provides:
- UpperCaseCharField: stores text in upper case on save.
- PhoneNumberField: simple phone number field with basic validation.
"""

from typing import Any

from django.db import models
from django.core import exceptions


class UpperCaseCharField(models.CharField):
    """CharField that ensures stored value is uppercase.

    The conversion happens in `pre_save` so any assigned value is
    normalized before being written to the database.
    """
    description = "CharField that stores text in upper case"

    def pre_save(self, model_instance: Any, add: bool) -> Any:
        """Normalize the attribute value to upper case before saving.

        Args:
            model_instance: The model instance containing the field.
            add: True if this is an insert operation.

        Returns:
            The (possibly modified) value that will be saved.
        """
        value = getattr(model_instance, self.attname)
        if value is None:
            return value
        new_value = value.upper()
        setattr(model_instance, self.attname, new_value)
        return new_value


class PhoneNumberField(models.CharField):
    """A simple phone number field that validates allowed characters.

    This is intentionally permissive: it allows digits, spaces, dashes,
    parentheses and plus sign. More strict validation can be applied in
    forms or via custom validators.
    """
    description = "Simple phone number field (digits and + allowed)"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('max_length', 32)
        super().__init__(*args, **kwargs)

    def clean(self, value: Any, model_instance: Any) -> Any:
        """Validate and clean value before model field validation.

        Args:
            value: The value to validate.
            model_instance: The model instance (unused here).

        Returns:
            The cleaned value or raises `ValidationError`.
        """
        value = super().clean(value, model_instance)
        if value is None or value == '':
            return value
        # Basic validation: only digits, spaces, dashes and plus
        import re
        if not re.fullmatch(r"[\d\s\-\+()]+", str(value)):
            raise exceptions.ValidationError('Enter a valid phone number')
        return value
