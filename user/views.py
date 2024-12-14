from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_list_or_404
from .models import Driver
from .serializers import DriverSerializer


class DriverCreateView(generics.CreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [permissions.IsAdminUser]

class DriverUpdateView(generics.UpdateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [permissions.IsAdminUser]

class DriverDeleteView(generics.DestroyAPIView):
    queryset = Driver.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class DriverListView(generics.ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [permissions.AllowAny] # 모든 사용자가 보는 것 가능