"""censoProy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from censoIndigenasApp.views import UsuarioListaView, UsuarioDetalleView, UsuarioPersonalizadoView

from censoIndigenasApp.views import UsuarioListaView, UsuarioDetalleView, UsuarioPersonalizadoView
from censoIndigenasApp import views as censo_views

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('censoIndigena/', include('censoIndigenasApp.urls')),

    path('usuarios/', UsuarioListaView.as_view()),                          # Ver y crear usuarios
    path('usuarios/<int:id_usuario_url>', UsuarioDetalleView.as_view()),    # _RUD usuario especificado
    path('perfil/', UsuarioPersonalizadoView.as_view()),                    # _RUD usuario autenticado

    path('ocupaciones/', censo_views.OcupacionList.as_view()),
    path('ocupaciones/<int:id_ocupacion_url>', censo_views.OcupacionDetail.as_view()),
    #path('ocupaciones/agregar/', censo_views.OcupacionCrearView.as_view()),

    path('etnias/', censo_views.EtniaList.as_view()),
    path('enias/<int:id_etnia_url>', censo_views.etniaDetail.as_view()),
    #path('etnias/agregar/', censo_views.EtniaCrearView.as_view()),

    path('resguardos/', censo_views.ResguardoList.as_view()),
    path('resguardos/<int:id_etnia_url>', censo_views.resguardoDetail.as_view()),
    #path('resguardos/agregar/', censo_views.ResguardoCrearView.as_view()),


    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
]
