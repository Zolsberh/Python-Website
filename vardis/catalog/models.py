from django.db import models
from django.urls import reverse


class Catalog(models.Model):

    title = models.CharField(max_length=200, verbose_name='Название каталога')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Изображение')
    is_display = models.BooleanField(default=True, verbose_name='Отображать')

    def __str__(self):
        return str(self.title)

    def get_name_catalog(self):
        return self.title

    def get_absolute_url(self):
        return reverse('catalog', kwargs={'catalog_slug': self.slug})

    class Meta:

        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'
        # ordering = ['-time_created']


class ProductCategory(models.Model):
    number = models.CharField(max_length=10, verbose_name='Номер')
    name = models.CharField(max_length=255, verbose_name='Категория')
    catalog = models.ForeignKey(Catalog, on_delete=models.PROTECT, verbose_name='Каталог', related_name='categories')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Изображение')
    is_display = models.BooleanField(default=True, verbose_name='Отображать')

    def __str__(self):
        return str(f'{self.number}. {self.name}')

    def get_absolute_url(self):
        return reverse('product_category', kwargs={'product_category_slug': self.slug})

    class Meta:
        ordering = ['pk']
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории товара'


class Product(models.Model):
    article = models.CharField(max_length=20, verbose_name='Артикул')
    name = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    # photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Изображение')
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, verbose_name='Категория')
    dimensions = models.TextField(blank=True, verbose_name='Габариты')
    description = models.TextField(blank=True, verbose_name='Описание')
    old_price = models.CharField(max_length=100, blank=True, verbose_name='Старая цена')
    new_price = models.CharField(max_length=100, blank=True, verbose_name='Новая цена')
    materials = models.ManyToManyField('MaterialCategory', verbose_name='Материал')
    is_new = models.BooleanField(default=True, verbose_name='Новинка')
    is_top = models.BooleanField(default=True, verbose_name='Топ продаж')
    is_availability = models.BooleanField(default=True, verbose_name='Наличие')
    is_display = models.BooleanField(default=True, verbose_name='Отображать')

    def __str__(self):
        return str(self.name)

    def get_image(self):
        return self.images.filter(product_id=self.id)[0].image.url

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return 'Изображение'

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Изображения'


class MaterialCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('material_category', kwargs={'material_category_slug': self.slug})

    class Meta:
        verbose_name = 'Тип материалов'
        verbose_name_plural = 'Образцы материалов'
        ordering = ['name']


class Material(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Изображение')
    category = models.ForeignKey(MaterialCategory, on_delete=models.CASCADE,
                                 verbose_name='Образец материалов', default=1, related_name='materials')
    is_display = models.BooleanField(default=True, verbose_name='Отображать')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'
