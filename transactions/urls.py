from django.urls import path

from .views import (
    TransactionCreateView, TransactionListView, 
    TransactionUpdateView, TransactionDeleteView
)

urlpatterns = [
    path('transaction/', TransactionCreateView.as_view(), name='transaction_create'),
    path('transaction/all/', TransactionListView.as_view(), name='transaction_list'),
    path('transaction/<int:pk>/update/', TransactionUpdateView.as_view(), name='transaction_update'),
    path('transaction/<int:pk>/delete/', TransactionDeleteView.as_view(), name='transaction_delete'),
]