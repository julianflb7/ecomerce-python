from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import CartProducts
from .models import Cart #Importa la clase Cart
from .utils import get_or_create_cart #Importa la función get_or_create_cart
from products.models import Product

# Create your views here.
def cart(request):
    """Crear un carrito de compras"""
    cart = get_or_create_cart(request) #Esta función se define en el archivo utils.py

    return render(request, 'carts/cart.html', {
        'cart':cart
    })

def add(request):
    """Agregar a el carrito"""
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))
    quantity = int(request.POST.get('quantity', 1))

    #cart.products.add(product, through_defaults={
    #    'quantity' : quantity
    #})

    cart_product = CartProducts.objects.create_or_update_quantity(cart=cart, #Este esa instancia que se le asigna un metodo de la clase CartProductsManager
                                                                    product=product,
                                                                    quantity=quantity)

    return render(request, 'carts/add.html', {
        'quantity' : quantity,
        'cart_product' : cart_product,
        'product' : product
    })


def remove(request):
    """Eliminar del carrito"""

    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))

    #Product.objects.get(pk=request.POST.get('product_id'))

    cart.products.remove(product)

    return redirect('carts:cart')
