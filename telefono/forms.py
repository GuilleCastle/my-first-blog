from django import forms

from telefono.models import Contacto

class contactoform(forms.ModelForm):

    class Meta:
        model = Contacto

        fields = [
            'nombre',
            'apellido',
            'grupo',
            'favorito',
        ]

