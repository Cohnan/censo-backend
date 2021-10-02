from django.urls import path
from .views import PersonaList

urlpatterns = [
    path('personas/', PersonaList.as_view()),
]