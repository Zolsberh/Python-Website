from django.contrib import admin
from .models import Slider, About, Contact, ContactPhone
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class AboutAdminForm(forms.ModelForm):

    class Meta:
        model = About
        fields = '__all__'

    description = forms.CharField(widget=CKEditorUploadingWidget, label='Описание')


class AboutAdmin(admin.ModelAdmin):
    form = AboutAdminForm
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_html_photo')
    list_display_links = ('id', 'title')
    list_filter = ('is_display',)

    def get_html_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100">')

    get_html_photo.short_description = 'Миниатюра'


class PhoneNumberInline(admin.StackedInline):
    model = ContactPhone
    max_num = 10
    extra = 0


class ContactAdmin(admin.ModelAdmin):
    inlines = [PhoneNumberInline]

    list_display = ('id', 'name', 'is_display')
    list_display_links = ('id', 'name')
    list_editable = ('is_display',)


admin.site.register(Slider, SliderAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Contact, ContactAdmin)
