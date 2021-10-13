from django.urls import path
from .views import PersonaListaView
from .views import PersonaDetailView
from .views import PersonaCrearView

urlpatterns = [
    path('personas/', PersonaListaView.as_view()),
    path('personas/<int:id>', PersonaDetailView.as_view()),
    path('censar/', PersonaCrearView.as_view())
]