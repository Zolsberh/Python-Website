from django.views.generic import ListView

from catalog.models import Catalog
from catalog.utils import DataMixin
from .models import About, Contact


class CatalogList(DataMixin, ListView):
    model = Catalog
    template_name = 'main/index.html'
    context_object_name = 'catalogs'

    def get_queryset(self):
        return Catalog.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Наши направления:')
        context.update(c_def)
        return context


class ShowAbout(ListView):
    template_name = 'main/about.html'
    model = About
    context_object_name = 'about'

    def get_queryset(self):
        return About.objects.get(pk=1)


class ContactList(DataMixin, ListView):
    template_name = 'main/contacts.html'
    model = Contact
    context_object_name = 'contacts'

    def get_queryset(self):
        return Contact.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Контакты')
        context.update(c_def)
        return context



