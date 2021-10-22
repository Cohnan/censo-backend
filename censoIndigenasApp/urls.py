from django.urls import path
from .views import PersonaListaView
from .views import PersonaDetailView
from .views import PersonaCrearView
from .views import PersonaBuscarDocView

urlpatterns = [
    path('personas/', PersonaListaView.as_view()),
    path('personas/<int:id>', PersonaDetailView.as_view()),
    path('censar/', PersonaCrearView.as_view()),
    path('buscar_doc/', PersonaBuscarDocView.as_view())
]