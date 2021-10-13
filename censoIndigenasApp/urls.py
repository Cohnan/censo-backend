from django.urls import path
from .views import PersonaList
from .views import PersonaDetail
from .views import PersonaCrearView

urlpatterns = [
    path('personas/', PersonaList.as_view()),
    path('personas/<int:id>', PersonaDetail.as_view()),
    path('personas/censar/', PersonaCrearView.as_view())
]