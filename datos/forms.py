from django import forms
from datos.models import Datos


class AddDatos(forms.ModelForm):
    '''
    fecha = forms.DateField(label='Fecha')
    entrada = forms.FloatField(label='Entrada')
    salida = forms.FloatField(label='Salida')
    total = forms.FloatField(label='Total')
    '''


    class Meta:
        model = Datos
        fields = ['fecha', 'concepto',  'ingreso', 'gasto',  'total']
        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control'}),
            'concepto': forms.TextInput(attrs={'class': 'form-control'}),
            'ingreso': forms.NumberInput(attrs={'class': 'form-control', 'v-model': 'ingreso'}),
            'gasto': forms.NumberInput(attrs={'class': 'form-control', 'v-model': 'gasto'}),
            'total': forms.NumberInput(attrs={'class': 'form-control', 'v-model': 'setTotal', 'readonly': 'readonly'})

        }








