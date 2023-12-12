from django.shortcuts import render
from django.http import HttpResponse
from .models import Emlak  # Emlak modelini içe aktarın

def category_emlak(request, id, slug):
    # Burada kategoriye özgü işlemleri yapabilirsiniz
    # Örneğin, belirli bir kategoriye ait emlakları getirin
    emlaklar = Emlak.objects.filter(category_id=id)

    # Görünüme gelen veriyi bir şablona iletmek için kullanabilirsiniz
    context = {
        'emlaklar': emlaklar,
        'category_id': id,
        'category_slug': slug,
    }
    return render(request, 'category_emlak.html', context)

def hakkimizda(request):
    # Hakkımızda sayfası görünümü
    return render(request, 'hakkimizda.html')


def contact_us(request):
    # İletişim sayfası görünümü
    return render(request, 'contact.html')

def index(request):
    # Anasayfa görünümü
    return render(request, 'index.html')