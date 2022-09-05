from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path("api/signup/", views.CreateUserView.as_view()),
]
