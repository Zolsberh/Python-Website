from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import *


class ProductAdminForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    dimensions = forms.CharField(widget=CKEditorUploadingWidget, label='Габариты')
    description = forms.CharField(widget=CKEditorUploadingWidget, label='Описание')


class CatalogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'get_html_photo', 'time_created', 'time_update', 'is_display')
    list_display_links = ('id', 'title')
    search_fields = ('title__iregex',)
    list_editable = ('is_display',)
    list_filter = ('is_display', 'time_created')
    fields = ('title', 'slug', 'photo', 'get_html_photo', 'is_display',)
    readonly_fields = ('get_html_photo', 'time_created', 'time_update')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width="100">')

    get_html_photo.short_description = 'Миниатюра'


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    max_num = 10
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm

    prepopulated_fields = {'slug': ('article', 'name',)}
    list_display = ('id', 'article', 'name', 'get_html_photo', 'dimensions', 'description', 'old_price', 'new_price',
                    'is_new', 'is_availability', 'is_display')
    list_display_links = ('id', 'name')
    search_fields = ('name__iregex', 'article__iregex', 'description__iregex')
    list_editable = ('is_display',)
    list_filter = ('is_display', 'is_new', 'is_availability')
    save_on_top = True
    fields = ('name', 'slug', 'get_html_photo', 'is_display',)
    readonly_fields = ('get_html_photo', 'is_new', 'is_availability')

    inlines = [ProductImageInline]

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width="100">')

    get_html_photo.short_description = 'Миниатюра'


class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('number', 'name',)}


class MaterialAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class MaterialCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(MaterialCategory, MaterialCategoryAdmin)
admin.site.register(Material, MaterialAdmin)

