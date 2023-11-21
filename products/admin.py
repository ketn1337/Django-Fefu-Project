from django.contrib import admin

from .models import Category, Product


class CategoryInline(admin.TabularInline):
    model = Category

class ProductInline(admin.TabularInline):
    model = Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
    )
    fields = ['title', 'slug']
    inlines = [ProductInline]



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'vendor',
        'title',
        'price',
        'slug',
        'description')
    
    fields = ['category', 'vendor', 'title', 'price', 'slug', 'description']

    
