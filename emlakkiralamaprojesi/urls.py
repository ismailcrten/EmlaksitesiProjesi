
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from user import views
from home import views
from user import views as Userviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emlak/', include('emlak.urls')),
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('', include('home.urls')),
    path ('user/', include('user.urls'), name='user'),
    path ('login/', Userviews.login_form, name='login_form'),
    path ('signup/', Userviews.signup_form, name='signup_form'),


    path('ckeditor/', include('ckeditor_uploader.urls')),  # ckeditor için URL'ler
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

