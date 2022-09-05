from django.db import models

from rest_framework import serializers
from django.contrib.auth import get_user_model


# Use get_user_model instead of importing the User model directly
# from django.contrib.auth.models import User
# This allows getting a custom user models instead if there was one
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    # The write_only option ensures the field may be used when updating or creating an instance,
    # but it is not included when serializing the representation.
    password = serializers.CharField(write_only=True)

    # The create method is provided by the ModelSerializer
    # But if needed method is essentially just: return ExampleModel.objects.create(**validated_data)
    def create(self, validated_data):
        """
        Create and return a new User instance, given the validated data.
        """
        # make sure to user create_user method and not create
        # the later will not know how to hash the password properly
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"],
        )
        return user

    class Meta:
        model = User
        fields = ("id", "username", "password", "email")
