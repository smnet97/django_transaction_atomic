from django.db import models

from product.models import Product


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_count = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
