"""Custom validators used in forms and models.

Contains simple validators for HEX colors and phone numbers.
"""

import re
from typing import Any

from django.core.exceptions import ValidationError


def hex_color_validator(value: Any) -> None:
    """Validate that `value` is a 6-digit HEX color (with optional #).

    Args:
        value: The value to validate.

    Raises:
        ValidationError: If the value does not match the HEX pattern.
    """
    if value is None or value == '':
        return
    if not re.fullmatch(r"#?[0-9a-fA-F]{6}", str(value)):
        raise ValidationError('Enter a valid HEX color (e.g. #aabbcc)')


def phone_validator(value: Any) -> None:
    """Basic phone validator allowing digits, space, dash, parentheses and plus.

    Note: This validator is permissive; use a stronger validator if needed.
    """
    if value is None or value == '':
        return
    if not re.fullmatch(r"[\d\s\-\+()]{6,32}", str(value)):
        raise ValidationError('Enter a valid phone number')
