from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_list_or_404
from .models import Division, Yard, Site, Master
from .serializers import YardSerializer, SiteSerializer, DivisionSerializer, MasterSerializer


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

class YardListView(generics.ListAPIView):
    queryset = Yard.objects.all()
    serializer_class = YardSerializer
    permission_classes = [permissions.AllowAny] # 모든 사용자가 보는 것 가능



class SiteCreateView(generics.CreateAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [permissions.IsAdminUser]

class SiteUpdateView(generics.UpdateAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [permissions.IsAdminUser]

class SiteDeleteView(generics.DestroyAPIView):
    queryset = Site.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class SiteListView(generics.ListAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [permissions.AllowAny] # 모든 사용자가 보는 것 가능



class DivisionCreateView(generics.CreateAPIView):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer
    permission_classes = [permissions.IsAdminUser]

class DivisionUpdateView(generics.UpdateAPIView):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer
    permission_classes = [permissions.IsAdminUser]

class DivisionDeleteView(generics.DestroyAPIView):
    queryset = Division.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class DivisionListView(generics.ListAPIView):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer
    permission_classes = [permissions.AllowAny] # 모든 사용자가 보는 것 가능



class MasterCreateView(generics.CreateAPIView):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer
    permission_classes = [permissions.IsAdminUser]

class MasterUpdateView(generics.UpdateAPIView):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer
    permission_classes = [permissions.IsAdminUser]

class MasterDeleteView(generics.DestroyAPIView):
    queryset = Master.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class MasterListView(generics.ListAPIView):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer
    permission_classes = [permissions.AllowAny] # 모든 사용자가 보는 것 가능