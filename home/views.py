
from django.shortcuts import render

from home.models import Setting

# Create your views here
# Create your views here

def index(request):
    setting = Setting.objects.get(pk=1)
    context = {
        'setting': setting
    }
    return render(request, template_name='index.html', context=context)

