from dataclasses import dataclass
from itertools import product

from django import forms

from .models import Order
from product.models import Product


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'order_count']

    def clean_order_count(self):
        if self.cleaned_data['product'].quantity < self.cleaned_data['order_count']:
            raise forms.ValidationError(f"Ushbu maxsulotdan faqat {self.cleaned_data['product'].quantity} ta qolgan !")

        return self.cleaned_data['order_count']
