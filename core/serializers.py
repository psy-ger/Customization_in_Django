"""DRF serializers for the `core` app models.

These serializers are used by the example API viewset.
"""

from rest_framework import serializers

from .models import CustomModel, RelatedItem, User


class RelatedItemSerializer(serializers.ModelSerializer):
    """Serializer for `RelatedItem` instances."""

    class Meta:
        model = RelatedItem
        fields = ('id', 'name', 'value')


class CustomModelSerializer(serializers.ModelSerializer):
    """Serializer for `CustomModel` that includes related items."""

    items = RelatedItemSerializer(many=True, read_only=True)

    class Meta:
        model = CustomModel
        fields = ('id', 'title', 'description', 'data', 'created', 'items')


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the custom `User` model."""

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number')
