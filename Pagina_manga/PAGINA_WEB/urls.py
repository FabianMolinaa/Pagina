from django.urls import path
from PAGINA_WEB import views

urlpatterns = [
    path("", views.index, name="index"),
    path('biblioteca/', views.biblioteca, name='biblioteca'),
]