from .models import Catalog


class DataMixin:
    paginate_by = 6

    def get_user_context(self, **kwargs):
        context = kwargs

        catalogs = Catalog.objects.all()
        context['catalogs'] = catalogs

        return context
