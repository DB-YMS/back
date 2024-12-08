from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_list_or_404
from .models import Division, Yard, Site, Master
from .serializers import YardSerializer


class YardCreateView(generics.CreateAPIView):
    queryset = Yard.objects.all()
    serializer_class = YardSerializer
    permission_classes = [permissions.IsAdminUser]

class YardUpdateView(generics.UpdateAPIView):
    queryset = Yard.objects.all()
    serializer_class = YardSerializer
    permission_classes = [permissions.IsAdminUser]

class YardDeleteView(generics.DestroyAPIView):
    queryset = Yard.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class YardListView(generics.ListAPIView): # yard 전체 보기
    queryset = Yard.objects.all()
    serializer_class = YardSerializer
    permission_classes = [permissions.AllowAny] # 모든 사용자가 보는 것 가능