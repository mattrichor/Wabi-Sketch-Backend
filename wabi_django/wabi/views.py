from django.shortcuts import render
from .models import User, Prompt, Sketch
from rest_framework import generics
from .serializers import UserSerializer, SketchSerializer, PromptSerializer
# Create your views here.


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PromptList(generics.ListCreateAPIView):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer


class PromptDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer


class SketchList(generics.ListCreateAPIView):
    queryset = Sketch.objects.all()
    serializer_class = SketchSerializer


class SketchDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sketch.objects.all()
    serializer_class = SketchSerializer
