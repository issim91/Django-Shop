from django.contrib import admin
from .models import *


class ProductImageInLine (admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductCategoryAdmin (admin.ModelAdmin):
    # выводит все поля таблицы
    list_display = [field.name for field in ProductCategory._meta.fields]

    class Meta:
        model = ProductCategory

admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductAdmin (admin.ModelAdmin):
    # выводит все поля таблицы
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInLine]

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)


class ProductImageAdmin (admin.ModelAdmin):
    # выводит все поля таблицы
    list_display = [field.name for field in ProductImage._meta.fields]

    class Meta:
        model = ProductImage

admin.site.register(ProductImage, ProductImageAdmin)
