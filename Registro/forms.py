from django import forms
from .models import Oferta

class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = ['nombre', 'fecha_vencimiento', 'nombre_proveedor','datos_contacto','detalles oferta', ]

        labels = {
            'nombre': 'Nombre del producto',
            'nombre_proveedor': 'Proveedor',
            'fecha_vencimiento': 'Fecha de caducidad de la oferta (opcional)',
            'datos_contacto': 'Datos de contacto',
            'detalles_oferta': 'Detalles',

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_proveedor': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_vencimiento': forms.DateInput(attrs={'class': 'form-control'}),
            'datos_contacto': forms.TextInput(attrs={'class': 'form-control'}),
            'detalles_oferta': forms.TextInput(attrs={'class': 'form-control'}),
           
        }
