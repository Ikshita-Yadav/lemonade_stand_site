from django.urls import path

from . import views

urlpatterns = [
    path('form/', views.sale_form, name='sale_form'),
    path('report/', views.report, name='report'),
]
