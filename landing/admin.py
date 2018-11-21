from django.contrib import admin
from .models import *

class SubscriberAdmin (admin.ModelAdmin):
    # list_display = ["id", "name", "email"]
    # выводит все поля таблицы
    list_display = [field.name for field in Subscriber._meta.fields]

    # Фильтр по полю
    list_filter = ["name"]

    # Поиск по конкретному полю
    search_fields = ["name"]

    # Не выводит поля, если перейти в запись
    # exclude = ["email"]
    # Выводит поля, если перейти в запись
    # fields = ["email"]

    class Meta:
        model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin)
