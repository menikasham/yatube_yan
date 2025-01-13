from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # импорт правил из приложения posts
    path('admin/', admin.site.urls),
    path('', include('posts.urls', namespace='posts')),
]
