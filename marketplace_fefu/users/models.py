from django.db import models
from django.contrib.auth.models import User

class Vendor(models.Model):

    user = models.OneToOneField(User, related_name='vendor', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()


    def get_balance(self):
        items = self.items.filter(vendor_paid=False, order__vendors__in=[self.id])
        return sum((item.product.price * item.quantity) for item in items)

    def get_paid_amount(self):
        items = self.items.filter(vendor_paid=True, order__vendors__in=[self.id])
        return sum((item.product.price * item.quantity) for item in items)