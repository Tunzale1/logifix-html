from rest_framework import serializers
from .models import Service  # Import your model

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"  # This will include all fields
