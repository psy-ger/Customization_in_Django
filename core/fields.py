from django.db import models
from django.core import exceptions


class UpperCaseCharField(models.CharField):
    description = "CharField that stores text in upper case"

    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname)
        if value is None:
            return value
        new_value = value.upper()
        setattr(model_instance, self.attname, new_value)
        return new_value


class PhoneNumberField(models.CharField):
    description = "Simple phone number field (digits and + allowed)"

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 32)
        super().__init__(*args, **kwargs)

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        if value is None or value == '':
            return value
        # Basic validation: only digits, spaces, dashes and plus
        import re
        if not re.fullmatch(r"[\d\s\-\+()]+", value):
            raise exceptions.ValidationError('Enter a valid phone number')
        return value
