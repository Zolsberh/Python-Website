from django.db import models


class Slider(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Изображение')
    is_display = models.BooleanField(default=True, verbose_name='Отображать')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'


class About(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О компании'
        verbose_name_plural = 'О компании'


class Contact(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    email = models.EmailField(max_length=255, verbose_name='Эл. почта')
    map = models.CharField(max_length=255, verbose_name='Адрес на карте')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    is_display = models.BooleanField(default=True, verbose_name='Отображать')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class ContactPhone(models.Model):
    number = models.CharField(max_length=255, verbose_name='Номер телефона')
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='phone_numbers')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Номер телефона'
        verbose_name_plural = 'Номера телефонов'

