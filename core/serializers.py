from rest_framework import serializers
from .models import CustomModel, RelatedItem, User


class RelatedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatedItem
        fields = ('id', 'name', 'value')


class CustomModelSerializer(serializers.ModelSerializer):
    items = RelatedItemSerializer(many=True, read_only=True)

    class Meta:
        model = CustomModel
        fields = ('id', 'title', 'description', 'data', 'created', 'items')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number')
