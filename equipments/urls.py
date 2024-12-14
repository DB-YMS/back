from django.urls import path

from .views import (
    EquipmentCreateView, EquipmentListView, EquipmentUpdateView, EquipmentDeleteView,
)

urlpatterns = [
    path('equipment/', EquipmentCreateView.as_view(), name='equipment_create'),
    path('equipment/all/', EquipmentListView.as_view(), name='equipment_list'),
    path('equipment/<int:pk>/update/', EquipmentUpdateView.as_view(), name='equipment_update'),
    path('equipment/<int:pk>/delete/', EquipmentDeleteView.as_view(), name='equipment_delete'),
]