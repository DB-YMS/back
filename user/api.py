from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status

class DriverList(APIView):
    def get(self, request):
        model = Driver.objects.all()
        serializer = DriverSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class DriverDetail(APIView):
    def get(self, request, driver_id):
        model = Driver.objects.get(driver_id = driver_id)
        serializer = DriverSerializer(model)
        return Response(serializer.data)

    def put(self, request, driver_id):
        model = Driver.objects.get(driver_id=driver_id)
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, driver_id):
        model = Driver.objects.get(driver_id=driver_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)