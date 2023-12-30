
from django.shortcuts import render
from emlak.models import Emlak, Category

from .models import Setting




def index(request):
    kategori = Category.objects.all()
    emlaklar = Emlak.objects.all()
    context = {'emlaklar': emlaklar,
               'kategori': kategori,}
    return render(request, 'index.html', context=context)


def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'hakkimizda'}
    return render(request, 'hakkimizda.html', context = context)

def iletisim(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'iletisim'}
    return render(request, 'iletisim.html', context = context)


