from django.contrib import admin
from unfold.admin import ModelAdmin
from . models import *

@admin.register(Category)
class Admin_cat(ModelAdmin):
    list_display=['category_id','category_name','printer_name', 'print_api']
    search_fields = ('name', 'printer_name')


@admin.register(Service)
class Admin_ser(ModelAdmin):
    list_display=['service_id','category','service_name','price']
    search_fields=('service_name',)


@admin.register(Order)
class Order_admin(ModelAdmin):
    list_display=['order_id','created_time','ordered_products']
    search_fields=('order_id',)


@admin.register(DeletedOrders)
class DeletedOrderAdmin(admin.ModelAdmin):
    list_display = ('deleted_order_id', 'reason', 'deleted_at')
    search_fields = ('reason',)
    filter_horizontal = ('services',)