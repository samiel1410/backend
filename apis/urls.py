from django.urls import path

from .views import ListPagos, DetailPagos

urlpatterns = [
    path('', ListPagos.as_view()),
    path('<int:pk>', DetailPagos.as_view())
]