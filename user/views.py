from django.shortcuts import render, redirect

from config.tasks import send_mail_task
from .forms import UserRegistrationForm
from django.conf import settings


def registration_view(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_mail_task.delay(
                subject="Xush kelibsiz !",
                message=f"Salom, {user.username} ! Bizni saytdan muvaffaqiyatli ro'yxatdan o'tdingiz.",
                recipient_list=[user.email],
            )
            return redirect('home')

    return render(request, 'registration.html', {"form": form})
