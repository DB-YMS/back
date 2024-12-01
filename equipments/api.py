from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status

class EquipmentList(APIView):
    def get(self, request):
        model = Equipment.objects.all()
        serializer = EquipmentSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EquipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



class EquipmentDetail(APIView):
    def get(self, request, equipment_id):
        model = Equipment.objects.get(equipment_id = equipment_id)
        serializer = EquipmentSerializer(model)
        return Response(serializer.data)

    def put(self, request, equipment_id):
        model = Equipment.objects.get(equipment_id=equipment_id)
        serializer = EquipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, equipment_id):
        model = Equipment.objects.get(equipment_id=equipment_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)