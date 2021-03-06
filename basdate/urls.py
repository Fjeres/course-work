from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.conf import settings

from news.views import get_general_information

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('cars/', include('cars.urls')),
    path('', get_general_information)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


