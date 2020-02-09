from django.http import request, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView
)

from datos.forms import AddDatos
from datos.models import Datos


class IndexView(TemplateView):
    template_name = 'datos/index.html'


class ListadoCompletoView(ListView):
    model = Datos
    paginate_by = 2

class CrearDatos(CreateView):
    model = Datos
    form_class = AddDatos
    success_url = reverse_lazy('datos_app:listado_completo')


class ActualizarDatos(UpdateView):
    model = Datos
    form_class = AddDatos
    template_name_suffix = '_update_form'

    def get_success_url(self):
       # return reverse_lazy('datos_app:actualizar_datos', args=[self.object.id])
        return reverse_lazy('datos_app:listado_completo')


class BorrarDato(DeleteView):
    model = Datos
    success_url = reverse_lazy('datos_app:listado_completo')


class ListadoIngresos(ListView):

    template_name = 'datos/listado_ingresos.html'
    context_object_name = 'ingresos'

    def get_queryset(self):

        #clave = self.request.GET.get('clave', '')
        lista = Datos.objects.filter(gasto=0)

        print(lista)

        return lista


def imprimir_todo(self, pk=None):

    import io
    from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle, Table
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter

    response = HttpResponse(content_type='application/pdf')
    buff = io.BytesIO()
    doc = SimpleDocTemplate(
        buff,
        pagesize=letter,
        leftMargin=40,
        rightMargin=40,
        topMargin=60,
        bottomMargin=18,
    )

    datos = []
    styles = getSampleStyleSheet()
    header = Paragraph('Listado Completo', styles['Heading2'])
    datos.append(header)
    headings = ('Fecha', 'Concepto', 'Ingreso', 'Gasto', 'Total')
    if not pk:
        registros = [(p.fecha, p.concepto, p.ingreso, p.gasto, p.total)
                     for p in Datos.objects.all().order_by('fecha')
                     ]
    else:
        registros = [(p.fecha, p.concepto, p.ingreso, p.gasto, p.total)
                     for p in Datos.objects.filter(id=pk).order_by('pk')
                     ]
    t = Table([headings] + registros)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))

    datos.append(t)
    doc.build(datos)
    response.write(buff.getvalue())
    buff.close()
    return response
