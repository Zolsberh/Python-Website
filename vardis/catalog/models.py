from django.db import models
from django.urls import reverse


class Catalog(models.Model):

    title = models.CharField(max_length=200, verbose_name='Название каталога')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Изображение')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_display = models.BooleanField(default=True, verbose_name='Отображать')

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('catalog', kwargs={'catalog_slug': self.slug})

    class Meta:

        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'
        ordering = ['-time_created']


class Category(models.Model):
    number = models.CharField(max_length=10, verbose_name='Номер')
    name = models.CharField(max_length=255, verbose_name='Категория')
    catalog = models.ForeignKey(Catalog, on_delete=models.PROTECT, verbose_name='Каталог')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Изображение')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_display = models.BooleanField(default=True, verbose_name='Отображать')

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    article = models.CharField(max_length=20, verbose_name='Артикул')
    name = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    # photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    dimensions = models.TextField(blank=True, verbose_name='Габариты')
    description = models.TextField(blank=True, verbose_name='Описание')
    old_price = models.CharField(max_length=100, blank=True, verbose_name='Старая цена')
    new_price = models.CharField(max_length=100, blank=True, verbose_name='Новая цена')
    materials = models.ManyToManyField('Material')
    is_new = models.BooleanField(default=True, verbose_name='Новинка')
    is_top = models.BooleanField(default=True, verbose_name='Топ продаж')
    is_availability = models.BooleanField(default=True, verbose_name='Наличие')
    is_display = models.BooleanField(default=True, verbose_name='Отображать')

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ProductImage(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')


class Material(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Изображение')

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('material', kwargs={'material_slug': self.slug})

    class Meta:
        verbose_name = 'Образец материала'
        verbose_name_plural = 'Образцы материалов'
