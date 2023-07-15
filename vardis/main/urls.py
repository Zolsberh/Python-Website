from django.urls import path
from . import views
from .views import CatalogList, ShowAbout, ContactList, SearchList

urlpatterns = [
    path('', CatalogList.as_view(), name='index'),
    path('about/', ShowAbout.as_view(), name='about'),
    path('contacts/', ContactList.as_view(), name='contacts'),
    path('search/', SearchList.as_view(), name='search'),
]
