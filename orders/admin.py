from django.contrib import admin
from .models import *


class ProductInOrderInLine (admin.TabularInline):
    model = ProductInOrder
    extra = 0


class StatusAdmin (admin.ModelAdmin):
    # выводит все поля таблицы
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)


class OrderAdmin (admin.ModelAdmin):
    # выводит все поля таблицы
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductInOrderInLine]

    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)


class ProductInOrderAdmin (admin.ModelAdmin):
    # выводит все поля таблицы
    list_display = [field.name for field in ProductInOrder._meta.fields]

    class Meta:
        model = ProductInOrder

admin.site.register(ProductInOrder, ProductInOrderAdmin)


class ProductInBasketAdmin (admin.ModelAdmin):
    # выводит все поля таблицы
    list_display = [field.name for field in ProductInBasket._meta.fields]

    class Meta:
        model = ProductInBasket

admin.site.register(ProductInBasket, ProductInBasketAdmin)
