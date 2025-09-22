from django.urls import path
from .views import RegisterView, PersonDetail
from . import views

urlpatterns = [
    path('person/<int:pk>/', PersonDetail.as_view(), name='person-detail'),

    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("me/", views.person_detail, name="person_detail"),
    path("me/", views.my_profile, name="my_profile"),

    path('api/register/', views.RegisterView.as_view(), name='api_register'),
    path('api/person/<int:pk>/', views.PersonDetail.as_view(), name='api_person_detail'),
]
