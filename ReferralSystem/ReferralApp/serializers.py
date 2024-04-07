# serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'referral_code']

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'referral_code', 'registration_timestamp']

class ReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'registration_timestamp']
