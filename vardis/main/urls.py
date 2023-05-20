from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('education/', views.education, name='education'),
    path('office/', views.office, name='office'),
    path('home/', views.home, name='home'),
]
