import re
from django.core.exceptions import ValidationError


def hex_color_validator(value):
    if value is None or value == '':
        return
    if not re.fullmatch(r"#?[0-9a-fA-F]{6}", value):
        raise ValidationError('Enter a valid HEX color (e.g. #aabbcc)')


def phone_validator(value):
    if value is None or value == '':
        return
    if not re.fullmatch(r"[\d\s\-\+()]{6,32}", value):
        raise ValidationError('Enter a valid phone number')
