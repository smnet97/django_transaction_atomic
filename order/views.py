from django.shortcuts import render, redirect
from django.db import transaction
from order.forms import OrderForm
from functools import partial

from product.models import Product


def send_email(username: str):
    print(f"Thanks {username} for your order")

def order_view(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                order = form.save()
                order.product.quantity -= order.order_count
                order.product.save()
            transaction.on_commit(partial(send_email, username="Ali"))
            return redirect('order')
    form.fields["product"].queryset = Product.objects.filter(quantity__gt=0)
    return render(request, 'order.html', context={
        "form": form
    })
