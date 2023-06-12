from django.contrib import admin
from catalog.models import Catalog, Product, ProductImage


class CatalogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    max_num = 10
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('article', 'name',)}
    inlines = [ProductImageInline]


admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Product, ProductAdmin)
