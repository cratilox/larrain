from django.urls import path, include
from . import views

urlpatterns = [
    #path('agregar_oferta', views.agregar_oferta, name="agregar_oferta"),
    
    path('listar_ofertas', views.listar_ofertas,name="listar_ofertas"),
    
    # CLASES GENERICAS
    path('add_oferta', views.OfertaCreate.as_view(), name="add_oferta"),
    
    path('edit_oferta/<int:pk>', views.OfertaUpdate.as_view(), name='edit_oferta'),
    ]