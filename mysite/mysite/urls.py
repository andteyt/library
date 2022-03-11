from django.urls import path

from library import views

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),

    path('book', views.book)

]