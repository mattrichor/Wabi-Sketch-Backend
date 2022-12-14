from rest_framework import serializers
from .models import User, Friends, Prompt, Sketch
from dataclasses import fields


from django.contrib.auth import get_user_model


# User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)
    # friends = serializers.HyperlinkedRelatedField(
    #     view_name='friends',
    #     many=True,
    #     read_only=True
    # )
    sketches = serializers.HyperlinkedRelatedField(
        view_name='sketch_detail',
        many=True,
        read_only=True
    )

    def create(self, validated_data):
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
        fields = ('id', 'email', 'username',
                  'password', 'is_active', 'sketches')


class FriendsSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Friends
        fields = ['user']


class FriendsWithSerializer(serializers.ModelSerializer):
    friend = UserSerializer()

    class Meta:
        model = Friends
        field = ['friends']


class PromptSerializer(serializers.HyperlinkedModelSerializer):
    sketches = serializers.HyperlinkedRelatedField(
        view_name='sketch_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Prompt
        fields = ('id', 'date', 'text', 'sketches')


class SketchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sketch
        fields = ('id', 'sketch_data', 'user', 'prompt')
