from django.contrib import admin
from .models import *

# Регистрация моделей
admin.site.register(Project)
admin.site.register(User)
admin.site.register(Text)
