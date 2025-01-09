from rest_framework import serializers
from .models import Equipment, DMEOrder, DMEOrderItem

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'

class DMEOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DMEOrder
        fields = '__all__'

class DMEOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DMEOrderItem
        fields = '__all__'