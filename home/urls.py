from django.urls import path

from home import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.Index.as_view(), name = 'index'),
    path('demo/', views.Upload, name = 'upload')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)