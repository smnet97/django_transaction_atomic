from django.shortcuts import render
from .models import Product
from config.tasks import my_task
from notification.models import NotificationModel
from django.utils import timezone
def home_view(request):
    q = request.GET.get('q')
    notifications = NotificationModel.objects.filter(sent=True, date__day=timezone.now().day)
    # products = Product.objects.filter(quantity__gt=0)
    # if q:
    #     products = products.filter(name__icontains=q)

    return render(request, 'home.html', context={
        # 'products': products,
        'notifications': notifications
    })
