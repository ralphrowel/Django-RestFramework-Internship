from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Person


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate_username(self, value):
        if " " in value:
            raise serializers.ValidationError("Username cannot contain spaces.")
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        Person.objects.create(
            user=user,
            person_firstname="",
            person_lastname="",
            person_age=0,
            person_gender="O",
            person_contact=None
        )
        return user


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
        read_only_fields = ['user']
