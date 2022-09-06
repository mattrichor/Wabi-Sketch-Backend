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
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer, SketchSerializer, PromptSerializer, MyTokenObtainPairSerializer

from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
# Create your views here.


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = UserSerializer


class CreateUserView(CreateAPIView):

    model = get_user_model
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = UserSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


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
def get_user(request, pk):
    profile = User.objects.get(id=pk)
    serializer = UserSerializer(profile, context={'user_id': pk})
    return JsonResponse(serializer.data)


@api_view(['GET'])
def getByPlayerName(request):
    player = User.objects.filter(name__iexact='Matthew Geyer')
    if len(player) > 0:
        serializer = serializers.serialize('json', player)
        return HttpResponse(serializer, content_type='application/json')
    else:
        return Response('oops!', status=400)


@api_view(['POST'])
def login(request):
    username = request.data['username']
    password = request.data['password']

    user = User.objects.get(username=username)

    if user is None:
        raise AuthenticationFailed('User does not exist!')

    if not user.check_password(password):
        raise AuthenticationFailed('Incorrect Password!')

    refresh = RefreshToken.for_user(user)

    return JsonResponse({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'payload': refresh.payload
    })
