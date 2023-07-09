from django.views.generic import ListView, DetailView

from catalog.models import ProductCategory, Product, Catalog
from catalog.utils import DataMixin


class CategoryList(DataMixin, ListView):
    model = ProductCategory
    template_name = 'catalog/categories.html'
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        catalog = Catalog.objects.get(slug=self.kwargs['catalog_slug'])
        c_def = self.get_user_context(title=catalog.title)
        context.update(c_def)
        return context

    def get_queryset(self):
        return ProductCategory.objects.filter(catalog__slug=self.kwargs['catalog_slug'])


class ProductList(DataMixin, ListView):
    model = Product
    template_name = 'catalog/products.html'
    context_object_name = 'products'
    allow_empty = False

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['product_category_slug'],
                                      is_display=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category = ProductCategory.objects.get(slug=self.kwargs['product_category_slug'])
        c_def = self.get_user_context(title=str(category))
        context.update(c_def)
        return context


class ShowProduct(DetailView):
    model = Product
    template_name = 'catalog/product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'
