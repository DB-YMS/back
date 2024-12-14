from django.urls import path

from .views import (
    DriverCreateView, DriverListView, DriverUpdateView, DriverDeleteView,
)

urlpatterns = [
    path('driver/', DriverCreateView.as_view(), name='driver_create'),
    path('driver/all/', DriverListView.as_view(), name='driver_list'),
    path('driver/<int:pk>/update/', DriverUpdateView.as_view(), name='driver_update'),
    path('driver/<int:pk>/delete/', DriverDeleteView.as_view(), name='driver_delete'),
]