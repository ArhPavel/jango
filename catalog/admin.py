from django.contrib import admin
from .models import Category, Product


admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'category', 'price', 'created_at', 'updated_at')

    list_display_links = ('id', 'name')

    search_fields = ('name', 'description')

    list_filter = ('category', 'created_at')