from rest_framework import serializers
from .models import Customer
from django.contrib.auth.hashers import make_password

class CustomerS(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields='__all__'

    def create(self, validated_data):
        # ✅ Hash password before saving
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)