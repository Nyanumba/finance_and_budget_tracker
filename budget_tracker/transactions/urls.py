from django.urls import path
from .views import TransactionListCreateView, TransactionDetailView, CategoryListCreateView, TransactionExportView

urlpatterns = [
    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('transactions/export/', TransactionExportView.as_view(), name='transaction-export'),
]