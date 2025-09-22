from django.urls import path
from .views import RegisterUserView, ListUsersView


urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('users/', ListUsersView.as_view(), name='list_users'),
]