from django.urls import path

from . import views

"""CON EL ATRIBUTO app_name SE LOGRA TENER RUTAS CON EL MISMO NOMBRE EN EL PROYECTO,
PUESTO QUE app_name DEFINE A QUE PROYECTO LE CORRESPONDE ESA LISTA DE DIRECCIONES urlpatterns
ES IMPORTANTE TENER CLARO QUE SI SE DEFINE DE ESTA FORMA SE DEBE BUSCAR EN EL CÓDIGO HTML EN
DONDE SE REALIZA EL LLAMADO A ESTAS DOS URL, TEMPLATES DE LA APLICACIÓN"""
app_name = 'products'

urlpatterns = [
    path('search', views.ProductSearchListView.as_view(), name='search'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product'),
]
