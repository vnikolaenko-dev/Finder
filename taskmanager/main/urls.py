from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

# Существующие URLS
urlpatterns = [
    # path('Путь', исполнитель)
    path('', views.index),
    path('profile/<user_id>', views.profile),
    path('profile', views.profile),
    path('create', views.create),
    path('create_note', views.create_note),
    path('projects', views.projects),
    path('project/<project_id>', views.project),
    path('login', views.signup),
    path('signup', views.login),
    path('subscriptions', views.subscriptions)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
