from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),       # Главная
    path('about/', views.about, name='about'),     # О нас
    path('faculties/', views.faculties, name='faculties'), # Факультеты
    path('admissions/', views.admissions, name='admissions'), # Поступающим
    path('contacts/', views.contacts, name='contacts'),   # Контакты
]