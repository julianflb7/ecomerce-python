from django.contrib import admin
from django.urls import path
from django.urls import include

from django.conf.urls.static import static #ESTO ES PARA LAS IMAGENES
from django.conf import settings #ESTO ES PARA LAS IMAGENES


from . import views

from products.views import ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('usuarios/login', views.login_view, name='login'),
    path('usuarios/logout', views.logout_view, name='logout'),
    path('usuarios/registro', views.register, name='register'),
    path('admin/', admin.site.urls),
    path('productos/', include('products.urls')),
    path('carrito/', include('carts.urls')),
    path('orden/', include('orders.urls')),
]

#LA SIGUIENTE CONDICION NOS PERMITE MOSTRAR LAS IMAGENES EN EL TEMPLATE
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
