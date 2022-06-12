from django.urls import path, include
from . import views
urlpatterns = [
    path('list_carrera', views.CarreraList.as_view(), name="list_carreras"),
    
    
    ]