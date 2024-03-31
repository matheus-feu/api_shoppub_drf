from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display: list[str] = ['name', 'description', 'price', 'stock', 'is_active']
    search_fields: list[str] = ['name', 'description']
    list_filter: list[str] = ['is_active']
    list_editable = ['is_active']


admin.site.register(Product, ProductAdmin)
