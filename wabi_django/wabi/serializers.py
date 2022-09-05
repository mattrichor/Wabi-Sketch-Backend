from rest_framework import serializers
from .models import Prompt, Sketch
from dataclasses import fields

from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # password = serializers.CharField(write_only=True)
    friends = serializers.HyperlinkedRelatedField(
        view_name='friends',
        many=True,
        read_only=True
    )
    sketches = serializers.HyperlinkedRelatedField(
        view_name='sketch_detail',
        many=True,
        read_only=True
    )

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
        fields = ('id', 'name', 'email', 'username',
                  'password', 'is_active', 'friends', 'sketches')


class PromptSerializer(serializers.HyperlinkedModelSerializer):
    sketches = serializers.HyperlinkedRelatedField(
        view_name='sketch_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Prompt
        fields = ('id', 'date', 'text', 'sketches')


class SketchSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )
    prompt = serializers.HyperlinkedRelatedField(
        view_name='prompt_detail',
        read_only=True
    )

    class Meta:
        model = Sketch
        fields = ('id', 'sketch_data', 'user', 'prompt')
