from django.shortcuts import render
from config.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail


# Create your views here.
# DataFlair #Send Email
def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Test'
        message = 'Test message'
        recepient = str(sub['Email'].value())
        send_mail(subject,
                  message, EMAIL_HOST_USER, [recepient], fail_silently=False)
        return render(request, 'common/success.html', {'recepient': recepient})
    return render(request, 'common/index.html', {'form': sub})
