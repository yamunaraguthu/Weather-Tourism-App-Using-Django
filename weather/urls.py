from django.urls import path
from .views import weather_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', weather_view, name='weather_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)