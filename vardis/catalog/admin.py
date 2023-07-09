from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from django.forms import CheckboxSelectMultiple

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
    list_display = ('id', 'title', 'get_html_photo',  'is_display')
    list_display_links = ('id', 'title')
    search_fields = ('title__iregex',)
    list_editable = ('is_display',)
    list_filter = ('is_display', 'title')
    readonly_fields = ('get_html_photo', )

    def get_html_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100">')

    get_html_photo.short_description = 'Миниатюра'


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    max_num = 10
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm

    prepopulated_fields = {'slug': ('article', 'name',)}
    list_display = ('id', 'article', 'name', 'get_html_photo', 'pr_price',
                    'is_new', 'is_availability', 'is_display')
    list_display_links = ('id', 'article', 'name')
    search_fields = ('name__iregex', 'article__iregex', 'description__iregex')
    list_editable = ('is_display',)
    list_filter = ('is_display', 'is_new', 'is_availability')
    save_on_top = True
    readonly_fields = ('get_html_photo', )

    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    inlines = [ProductImageInline]

    def pr_price(self, obj):
        return obj.new_price

    pr_price.short_description = 'Цена'

    def get_html_photo(self, obj):
        image_list = obj.images.all()
        if image_list:
            return mark_safe(f'<img src="{image_list[0].image.url}" width="100">')

    get_html_photo.short_description = 'Миниатюра'


class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('number', 'name',)}

    list_display = ('id', 'pc_name', 'get_html_photo', 'is_display')
    list_display_links = ('id', 'pc_name')
    search_fields = ('number__iregex', 'name__iregex', )
    list_editable = ('is_display',)
    list_filter = ('is_display',)
    readonly_fields = ('get_html_photo',)

    def pc_name(self, obj):
        return f'{obj.number}. {obj.name}'

    pc_name.short_description = 'Название'

    def get_html_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100">')

    get_html_photo.short_description = 'Миниатюра'


class MaterialAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'category_name', 'get_html_photo', 'is_display')
    readonly_fields = ('get_html_photo',)
    list_editable = ('is_display',)
    list_filter = ('is_display', 'category')
    search_fields = ('name__iregex', )
    list_display_links = ('id', 'name',)

    def category_name(self, obj):
        return obj.category.name

    category_name.short_description = 'Категория'

    def get_html_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100">')

    get_html_photo.short_description = 'Миниатюра'


class MaterialCategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name__iregex',)


admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(MaterialCategory, MaterialCategoryAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.site_header = 'Администрирование Вардис'
