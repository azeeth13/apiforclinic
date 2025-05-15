from django.urls import path
from .views import (
    CategoryListCreateView, CategoryDetailView,
    ServiceListCreateView, ServiceDetailView,
    OrderListCreateView, OrderDetailView, OrderDeleteWithReasonView,
    DeletedOrderListView
)

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('services/', ServiceListCreateView.as_view(), name='service-list-create'),
    path('services/<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('orders/<int:pk>/delete/', OrderDeleteWithReasonView.as_view(), name='order-delete-reason'),
    path('deleted-orders/', DeletedOrderListView.as_view(), name='deleted-order-list'),
]
