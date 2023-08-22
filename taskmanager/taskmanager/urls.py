from django.contrib import admin
from django.urls import path, include

# Существующие URLS
urlpatterns = [
    # include подключает main.urls для работы
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('about', include('main.urls')),
    path('projects', include('main.urls')),
    path('project/<project_id>', include('main.urls')),
    path('login', include('main.urls')),
    path('signup', include('main.urls'))
]
