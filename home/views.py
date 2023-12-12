from django.shortcuts import render
from .models import Setting

def index(request):
    setting = Setting.objects.get(pk=1)  # Varsayılan olarak setting'in ID'si 1 olduğunu varsayıyorum
    context = {
        'setting': setting,
        'page': 'home'
    }
    return render(request, 'index.html', context=context)


def hakkimizda(request):
    setting = Setting.objects.get(pk=1)  # Varsayılan olarak setting'in ID'si 1 olduğunu varsayıyorum
    context = {'setting': setting, 'page': 'hakkimizda'}
    return render(request, 'hakkimizda.html', context = context)


