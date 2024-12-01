from ctypes.wintypes import DOUBLE
from tkinter.constants import SOLID

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status

class DivisionList(APIView):
    def get(self, request):
        model = Division.objects.all()
        serializer = DivisionSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DivisionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class DivisionDetail(APIView):
    def get(self, request, division_id):
        model = Division.objects.get(division_id = division_id)
        serializer = DivisionSerializer(model)
        return Response(serializer.data)

    def put(self, request, division_id):
        model = Division.objects.get(division_id=division_id)
        serializer = DivisionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, division_id):
        model = Division.objects.get(division_id=division_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class MasterList(APIView):
    def get(self, request):
        model = Master.objects.all()
        serializer = MasterSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MasterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class MasterDetail(APIView):
    def get(self, request, id):
        model = Master.objects.get(id = id)
        serializer = MasterSerializer(model)
        return Response(serializer.data)

    def put(self, request, id):
        model = Master.objects.get(id=id)
        serializer = MasterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        model = Master.objects.get(id=id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class SiteList(APIView):
    def get(self, request):
        model = Site.objects.all()
        serializer = SiteSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SiteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class SiteDetail(APIView):
    def get(self, request, site_id):
        model = Site.objects.get(site_id = site_id)
        serializer = SiteSerializer(model)
        return Response(serializer.data)

    def put(self, request, site_id):
        model = Site.objects.get(site_id=site_id)
        serializer = SiteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, site_id):
        model = Site.objects.get(site_id=site_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class YardList(APIView):
    def get(self, request):
        model = Yard.objects.all()
        serializer = YardSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = YardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class YardDetail(APIView):
    def get(self, request, yard_id):
        model = Yard.objects.get(yard_id = yard_id)
        serializer = YardSerializer(model)
        return Response(serializer.data)

    def put(self, request, yard_id):
        model = Yard.objects.get(yard_id=yard_id)
        serializer = YardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, yard_id):
        model = Yard.objects.get(yard_id=yard_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)