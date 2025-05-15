# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Service, Order, DeletedOrders
from .serializers import CategorySerializer, ServiceSerializer, OrderSerializer, DeletedOrderSerializer
from django.shortcuts import get_object_or_404

# Category
class CategoryListCreateView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class CategoryDetailView(APIView):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return Response(status=204)

# Service
class ServiceListCreateView(APIView):
    def get(self, request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ServiceDetailView(APIView):
    def get(self, request, pk):
        service = get_object_or_404(Service, pk=pk)
        serializer = ServiceSerializer(service)
        return Response(serializer.data)

    def put(self, request, pk):
        service = get_object_or_404(Service, pk=pk)
        serializer = ServiceSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        service = get_object_or_404(Service, pk=pk)
        service.delete()
        return Response(status=204)

class OrderListCreateView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        service_ids = request.data.get('service_ids')
        if not service_ids:
            return Response({"error": "service_ids required"}, status=400)

        order = Order.objects.create()
        order.services.set(service_ids)
        order.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=201)

class OrderDetailView(APIView):
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

class OrderDeleteWithReasonView(APIView):
    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        reason = request.data.get('reason')
        if not reason:
            return Response({"error": "Reason is required"}, status=400)

        deleted_order = DeletedOrders.objects.create(reason=reason)
        deleted_order.services.set(order.services.all())
        deleted_order.save()
        order.delete()
        return Response({"message": "Order deleted and saved to DeletedOrders"}, status=200)

class DeletedOrderListView(APIView):
    def get(self, request):
        deleted_orders = DeletedOrders.objects.all()
        serializer = DeletedOrderSerializer(deleted_orders, many=True)
        return Response(serializer.data)
