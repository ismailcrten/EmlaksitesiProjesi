
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from emlak import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emlak/', include('emlak.urls')),
    path ('hakkimizda/',views.hakkimizda, name='hakkimizda' ),# emlak uygulamasının URL'leri
    path('', include('home.urls')),  # Ana sayfa için home uygulamasının URL'leri
    path('ckeditor/', include('ckeditor_uploader.urls')),  # ckeditor için URL'ler
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

