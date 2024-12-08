from django.urls import path
from .views import (
    YardCreateView, YardUpdateView, YardDeleteView, YardListView
)

urlpatterns = [
    path('yard/', YardCreateView.as_view(), name='yard_create'),
    path('yard/all/', YardListView.as_view(), name='yard_list'),
    path('yard/<int:pk>/update/', YardUpdateView.as_view(), name='yard_update'),
    path('yard/<int:pk>/delete/', YardDeleteView.as_view(), name='yard_delete'),
]