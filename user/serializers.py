from rest_framework import serializers
from .models import Driver

class DriverSerializer(serializers.ModelSerializer):
    driver_id = serializers.CharField(required=False)

    class Meta:
        model = Driver
        fields = '__all__'