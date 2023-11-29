from django.db import models
from shop.models import Product

# Create your models here.
class Cart(models.Model):
    cart_id=models.CharField(max_length=250,blank=True)
    date_added=models.DateField(auto_now_add=True)

    class Meta:
        ordering=['date_added']
        db_table='Cart'

    def __str__(self):
        return '{}'.format(self.cart_id)

class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)

    class Meta:
        db_table='CartItem'

    def __str__(self):
        return '{}'.format(self.product)

    def sub_total(self):
        return self.product.price * self.quantity
