from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from .models import Equipment, DMEOrder, DMEOrderItem
from .serializers import EquipmentSerializer, DMEOrderItemSerializer, DMEOrderSerializer

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

class EquipmentOrderViewSet(viewsets.ModelViewSet):
    queryset = DMEOrder.objects.all()
    serializer_class = DMEOrderSerializer
    permission_classes = [IsAuthenticated]

class EquipmentOrderItemViewSet(viewsets.ModelViewSet):
    queryset = DMEOrderItem.objects.all()
    serializer_class = DMEOrderItemSerializer
    permission_classes = [IsAuthenticated]