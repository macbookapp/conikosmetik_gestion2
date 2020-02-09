from django.urls import include, path, re_path
from .views import IndexView, ListadoCompletoView, CrearDatos, ActualizarDatos, BorrarDato, ListadoIngresos,\
    imprimir_todo


app_name = 'datos_app'

urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('listado_completo/', ListadoCompletoView.as_view(), name='listado_completo'),
    path('crear_dato/', CrearDatos.as_view(), name='crear_datos'),
    path('actualizar_datos/<int:pk>/', ActualizarDatos.as_view(), name='actualizar_datos'),
    path('borrar_datos/<int:pk>/', BorrarDato.as_view(), name='borrar_dato'),
    path('listado_ingresos', ListadoIngresos.as_view(), name='listado_ingresos'),
    path('imprimir', imprimir_todo, name='imprimir_todo'),
    path('imprimir/<int:pk>', imprimir_todo, name='imprimir_uno'),


]