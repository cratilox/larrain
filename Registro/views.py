from django.shortcuts import render, redirect
from .models import Oferta
from .forms import OfertaForm
# las clases genericas
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# esta libreria nos permitira redireccionamiento
from django.urls import reverse_lazy

class CarreraList(ListView):
    model = Oferta
    template_name = 'Oferta/list_carreras.html'
    # paginate_by = 4



def listar_ofertas(request):
        # SELECT * FROM CARRERA
    ofertas = Oferta.objects.all()
    return render(request, "Registro/listar_ofertas.html", 
                  {'oferta': ofertas})

