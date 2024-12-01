from rest_framework import serializers
from .models import Equipment

class EquipmentSerializer(serializers.ModelSerializer):
    equipment_id = serializers.CharField(required=False)
    equipment_type = serializers.CharField(required=False)
    equipment_sort = serializers.CharField(required=False)
    status = serializers.CharField(required=False)
    # 빈 값이어도 되는 것들(not null의 반대..?랑 비슷한 것 같음) equipment_id는 notnull이므로 수정필요


    class Meta:
        model = Equipment
        fields = '__all__'