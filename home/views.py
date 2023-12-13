from django.shortcuts import render
from django.template import loader
from emlak.models import Emlak

from .models import Setting


def index(request):
    setting = Setting.objects.get(pk=1)  # Varsayılan olarak setting'in ID'si 1 olduğunu varsayıyorum
    context = {
        'setting': setting,
        'page': 'home'
    }
    return render(request, 'index.html', context=context)


def index(request):
    template = loader.get_template('index.html')
    context = {}

    emlak = Emlak.objects.all()
    if bool(emlak):
        n = len(emlak)
        nslide = n // 3 + (n % 3 > 0)
        rooms = [emlak, range(1, nslide), n]
        context.update({'emlak': emlak})
    return render(request, 'index.html', context)


def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'hakkimizda'}
    return render(request, 'hakkimizda.html', context = context)

def iletisim(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'iletisim'}
    return render(request, 'iletisim.html', context = context)


