from django.urls import path
from .views import PersonaList
from .views import PersonaDetail

urlpatterns = [
    path('personas/', PersonaList.as_view()),
    path('personas/<int:id>', PersonaDetail.as_view())
]