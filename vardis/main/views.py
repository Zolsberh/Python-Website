from django.views.generic import ListView
from django.db.models import Q

from catalog.models import Catalog, Product
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


class SearchList(DataMixin, ListView):
    model = Product
    template_name = 'main/search.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Результат поиска')
        context.update(c_def)
        return context

    def get_queryset(self):
        query = self.request.GET.get('query')
        products = Product.objects.filter(
            Q(article__icontains=query) | Q(name__icontains=query)
        )
        return products
