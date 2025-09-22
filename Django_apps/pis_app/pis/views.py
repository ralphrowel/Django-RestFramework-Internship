from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

from rest_framework import generics
from .models import Person
from .serializers import RegisterSerializer, PersonSerializer
from .forms import PersonForm


# --- API Views (for Postman / REST clients) ---
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class PersonDetail(generics.RetrieveUpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


# --- Regular HTML Views (for browser) ---
def home(request):
    return render(request, "pis/home.html")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Person.objects.create(user=user)
            login(request, user)
            return redirect("person_detail")
    else:
        form = UserCreationForm()
    return render(request, "pis/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("person_detail")
    else:
        form = AuthenticationForm()
    return render(request, "pis/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("home")


@login_required
def person_detail(request):
    person = Person.objects.get(user=request.user)
    return render(request, "pis/person_detail.html", {"person": person})

@login_required
def my_profile(request):
    person = request.user.person
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect("person_detail")
    else:
        form = PersonForm(instance=person)
    return render(request, "pis/my_profile.html", {"form": form})