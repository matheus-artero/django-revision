from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),

    path('read_all/', views.read_all, name='read_all'),
    path('update/<id>/', views.update, name='update'),
    path('delete/<id>/', views.delete, name='delete'),
]