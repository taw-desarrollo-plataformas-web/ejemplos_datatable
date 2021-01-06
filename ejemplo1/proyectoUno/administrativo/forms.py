from django.forms import ModelForm
from django import forms
from administrativo.models import Estudiante, NumeroTelefonico


class EstudianteForm(ModelForm): 
    class Meta:
        model = Estudiante 
        fields = ['nombre', 'apellido', 'cedula'] 


class NumeroTelefonicoForm(ModelForm): 
    
    def __init__(self, estudiante, *args, **kwargs):
        super(NumeroTelefonicoForm, self).__init__(*args, **kwargs)
        self.fields['estudiante'] = forms.CharField(initial = estudiante.id, 
              widget=forms.HiddenInput())

    class Meta:
        model = NumeroTelefonico 
        fields = ['telefono', 'tipo'] 
        exclude = ('estudiante',)
        




