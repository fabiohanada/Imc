from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('calcular_imc/<int:pessoa_id>', views.calcular_imc_view, name='calcular_imc'),
]