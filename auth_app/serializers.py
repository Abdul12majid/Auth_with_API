from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields=('first_name', 'last_name', 'username', 'password', 'email', )

class MySerializer(serializers.Serializer):
	username=serializers.CharField()
	password=serializers.CharField()

class PasswordSerializer(serializers.Serializer):
	old_password=serializers.CharField()
	new_password=serializers.CharField()
	confirm_password=serializers.CharField()

class SignupSerializer(serializers.Serializer):
	first_name=serializers.CharField()
	last_name=serializers.CharField()
	username=serializers.CharField()
	password=serializers.CharField()
	email=serializers.EmailField()