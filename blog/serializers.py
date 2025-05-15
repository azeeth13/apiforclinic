from rest_framework import serializers
from .models import Category, Service, Order, DeletedOrders

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)
    service_ids = serializers.PrimaryKeyRelatedField(
        queryset=Service.objects.all(), many=True, write_only=True, source='services'
    )

    class Meta:
        model = Order
        fields = ['order_id', 'services', 'service_ids', 'created_at']

class DeletedOrderSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = DeletedOrders
        fields = '__all__'