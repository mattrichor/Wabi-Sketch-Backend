from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('users', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetails.as_view(), name='user_detail'),
    path('prompts', views.PromptList.as_view(), name='prompt_list'),
    path('prompts/<int:pk>', views.PromptDetails.as_view(), name='prompt_detail'),
    path('sketches', views.SketchList.as_view(), name='sketch_list'),
    path('sketches/<int:pk>', views.SketchDetails.as_view(), name='sketch_detail'),
    path('test', views.getByPlayerName, name='rand_json'),
]
