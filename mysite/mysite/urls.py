from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from library import views

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/<int:book_id>/', views.book),
    path('', views.index),
    path('author/<int:author_id>/', views.author),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)