"""Forms for the `core` application with custom validators and fields."""

from typing import Any, Optional

from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomModel, User
from .validators import hex_color_validator, phone_validator


class HexColorFormField(forms.CharField):
    """Form field that validates HEX color values (e.g. `#aabbcc`)."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('max_length', 7)
        super().__init__(*args, **kwargs)

    def validate(self, value: Any) -> None:
        super().validate(value)
        hex_color_validator(value)


class PhoneFormField(forms.CharField):
    """Form field that validates phone numbers using `phone_validator`."""

    def validate(self, value: Any) -> None:
        super().validate(value)
        phone_validator(value)


class CustomModelForm(forms.ModelForm):
    """ModelForm for `CustomModel` with an additional optional color field."""

    color = HexColorFormField(required=False)

    class Meta:
        model = CustomModel
        fields = ['title', 'description', 'data']

    def clean_title(self) -> str:
        title = self.cleaned_data['title']
        # custom validator: title must be at least 3 chars
        if len(title.strip()) < 3:
            raise forms.ValidationError('Title is too short')
        return title


class RegistrationForm(UserCreationForm):
    """User registration form using the custom `User` model."""

    phone_number = PhoneFormField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number')

    def clean_phone_number(self) -> Optional[str]:
        phone = self.cleaned_data.get('phone_number')
        phone_validator(phone)
        return phone
