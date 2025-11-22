from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomModel, User, RelatedItem
from .validators import hex_color_validator, phone_validator
from .fields import PhoneNumberField


class HexColorFormField(forms.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 7)
        super().__init__(*args, **kwargs)

    def validate(self, value):
        super().validate(value)
        hex_color_validator(value)


class PhoneFormField(forms.CharField):
    def validate(self, value):
        super().validate(value)
        phone_validator(value)


class CustomModelForm(forms.ModelForm):
    color = HexColorFormField(required=False)

    class Meta:
        model = CustomModel
        fields = ['title', 'description', 'data']

    def clean_title(self):
        title = self.cleaned_data['title']
        # custom validator: title must be at least 3 chars
        if len(title.strip()) < 3:
            raise forms.ValidationError('Title is too short')
        return title


class RegistrationForm(UserCreationForm):
    phone_number = PhoneFormField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number')

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        phone_validator(phone)
        return phone
