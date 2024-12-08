from rest_framework import serializers
from .models import Division, Master, Site, Yard

class DivisionSerializer(serializers.ModelSerializer):
    division_id = serializers.IntegerField(required=False)
    division_name = serializers.CharField(required=False)

    class Meta:
        model = Division
        fields = '__all__' # Division에 있는 모든 값 출력


class MasterSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Master
        fields = '__all__' # Master에 있는 모든 값 출력


class SiteSerializer(serializers.ModelSerializer):
    site_id = serializers.IntegerField(required=False)
    capacity = serializers.IntegerField(required=False)
    current_quantity = serializers.IntegerField(required=False)

    class Meta:
        model = Site
        fields = '__all__' # Site에 있는 모든 값 출력


class YardSerializer(serializers.ModelSerializer):
    yard_id = serializers.IntegerField(required=False)

    class Meta:
        model = Yard
        fields = '__all__'

