from django.db import models
from django.urls import reverse


class Catalog(models.Model):

    title = models.CharField(max_length=200, verbose_name='Название каталога')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Изображение')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('catalog', kwargs={'catalog_slug': self.slug})

    class Meta:

        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'
        ordering = ['-time_created']
