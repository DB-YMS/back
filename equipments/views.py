from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_list_or_404
from .models import Equipment
from .serializers import EquipmentSerializer


class EquipmentCreateView(generics.CreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [permissions.IsAdminUser]

class EquipmentUpdateView(generics.UpdateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [permissions.IsAdminUser]

class EquipmentDeleteView(generics.DestroyAPIView):
    queryset = Equipment.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class EquipmentListView(generics.ListAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [permissions.AllowAny] # 모든 사용자가 보는 것 가능