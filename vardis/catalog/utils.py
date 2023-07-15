from .models import ProductCategory, Catalog


class DataMixin:
    paginate_by = 6

    def get_user_context(self, **kwargs):
        context = kwargs

        if 'catalog_title' in context.keys():
            catalog_title = context['catalog_title']
            cat_menu = ProductCategory.objects.filter(catalog__title=catalog_title)
        else:
            cat_menu = Catalog.objects.all()
        context['cat_menu'] = cat_menu

        return context
