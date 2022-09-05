from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
from .models import User, Prompt, Sketch
from rest_framework import generics
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .serializers import UserSerializer, SketchSerializer, PromptSerializer
# Create your views here.


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny,  # Unauthenticated users must be able to sign up
    ]
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = UserSerializer


class CreateUserView(CreateAPIView):

    model = User
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = UserSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email

        return token


class PromptList(generics.ListCreateAPIView):
    queryset = Prompt.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = PromptSerializer


class PromptDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prompt.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = PromptSerializer


class SketchList(generics.ListCreateAPIView):
    queryset = Sketch.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = SketchSerializer


class SketchDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sketch.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = SketchSerializer


@api_view(['GET'])
def getByPlayerName(request):
    player = User.objects.filter(name__iexact='Matthew Geyer')
    if len(player) > 0:
        serializer = serializers.serialize('json', player)
        return HttpResponse(serializer, content_type='application/json')
    else:
        return Response('oops!', status=400)


@api_view(['POST'])
def loginUser(request):
    print('hello!')
