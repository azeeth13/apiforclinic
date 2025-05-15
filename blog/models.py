from django.db import models

class Category(models.Model):
    category_id=models.AutoField(primary_key=True)
    category_name=models.CharField(max_length=250)
    printer_name=models.CharField(max_length=255)
    print_api=models.CharField(max_length=255)

    def __str__(self):
        return self.category_name
    

class Service(models.Model):
    service_id=models.AutoField(primary_key=True)
    
    service_name=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10,decimal_places=2    )
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='services')
    


    def __str__(self):
        return self.service_name



class Order(models.Model):

    order_id=models.AutoField(primary_key=True)
    ordered_products=models.ForeignKey(Service,on_delete=models.CASCADE,related_name='orders')
    created_time=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.order_id}"
    


class DeletedOrders(models.Model):
    deleted_order_id = models.AutoField(primary_key=True)
    services = models.ManyToManyField(Service)
    deleted_at = models.DateTimeField(auto_now_add=True)
    reason = models.TextField()

    def __str__(self):
        return f"O'chirilgan servislar {self.deleted_order_id}"