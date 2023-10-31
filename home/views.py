from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    text = " merhaba "
    context = {"text": text}
    return render(request, "index.html", context)
    # return HttpResponse("Hello, world. You're at the polls index.") # http://
