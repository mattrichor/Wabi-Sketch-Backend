from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('users', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetails.as_view(), name='user_detail'),

    path('prompts', views.PromptList.as_view(), name='prompt_list'),
    path('prompts/<int:pk>', views.PromptDetails.as_view(), name='prompt_detail'),

    path('sketches', views.SketchList.as_view(), name='sketch_list'),
    path('sketches/save', views.save_sketch),

    path('sketches/<int:pk>', views.SketchDetails.as_view(), name='sketch_detail'),

    path('test', views.getByPlayerName, name='rand_json'),

    path("api/signup/", views.CreateUserView.as_view()),


    path('login/', views.login),
    path('user/<int:pk>/', views.get_user),
    # path('token/obtain/', jwt_views.TokenObtainPairView.as_view(),
    #      name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('lobby/', views.lobby)
]
