from django.contrib import admin

from lendapp.models import Category, Item, LendProduct,Location, ProductGallery,Keyword

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['area_name']
@admin.register(ProductGallery)
class ProductGalleryAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(Item)
class ProductGalleryAdmin(admin.ModelAdmin):
    list_display = ['title']
@admin.register(LendProduct)
class ProductGalleryAdmin(admin.ModelAdmin):
    list_display = ['user']
@admin.register(Keyword)
class ProductGalleryAdmin(admin.ModelAdmin):
    list_display = ['user']
