from django.shortcuts import render, redirect
from .forms import OfertaForm
from .models import Oferta
from django.urls import reverse_lazy
#Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

def listar_ofertas(request):
    # SELECT * FROM Oferta
    ofertas = Oferta.objects.all()
    return render(request, "Oferta/listar_ofertas.html", 
                 {'ofertas': ofertas})

class OfertaCreate(CreateView):
    model = Oferta
    form_class = OfertaForm
    template_name = 'Oferta/oferta_form.html'
    success_url = reverse_lazy("listar_ofertas")
    
class OfertaUpdate(UpdateView):
    model = Oferta
    form_class = OfertaForm
    template_name = 'Oferta/oferta_form.html'
    success_url = reverse_lazy('listar_ofertas')



#def agregar_oferta(request):
#    if request.method == "POST":
#        form = OfertaForm(request.POST)
#        if form.is_valid():
#            model_instance = form.save(commit=False)
#            model_instance.save()
#            return redirect("/agregar_carrera")
#    else:
#        form = OfertaForm()
#        return render(request, "Registro/agregar_carrera.html", {'form': form})