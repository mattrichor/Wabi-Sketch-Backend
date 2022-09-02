from rest_framework import serializers
from .models import User, Prompt, Sketch, Friend
from dataclasses import fields


class UserSerializer(serializers.HyperlinkedModelSerializer):
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
