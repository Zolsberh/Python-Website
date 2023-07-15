from django.http import HttpRequest
from django import template
from main.models import Slider, Contact
from catalog.models import Catalog


register = template.Library()


@register.inclusion_tag('main/megamenu.html')
def show_menu():
    catalogs = Catalog.objects.all()
    return {'catalogs': catalogs}


@register.inclusion_tag('main/slider.html')
def show_slider():
    slider_items = Slider.objects.all()
    return {'slider_items': slider_items}


@register.inclusion_tag('main/phonenumbers.html')
def show_numbers():
    contact = Contact.objects.get(name='Офис')
    phones = contact.phone_numbers.all()
    return {'phones': phones}
