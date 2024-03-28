from django.db import models
from accounts.models import Account, UserProfile
from store.models import Product, Variation


# Create your models here.
class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Packed', 'Packed'),
        ('On The Way', 'On The Way'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled')
    )
    PAYMENT_METHODS = (
        ('Stripe', 'Stripe'),
        ('COD', 'Cash on Delivery'),
    )

    user = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    order_number = models.CharField(max_length=20, blank=True, null=True)
    order_total = models.FloatField(blank=True, null=True)
    tax = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS, default='Pending')
    ip = models.CharField(blank=True, max_length=20)
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    shipping_address = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True) 
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS, default='COD') 

    def __str__(self):
        return self.order_number
    
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation, blank=True)
    quantity = models.IntegerField()
    product_price = models.FloatField()
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.product_name