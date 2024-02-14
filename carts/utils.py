
from .models import Cart #Importa la clase Cart de el archivo models.py

def get_or_create_cart (request):
    """Esta función crea un carrito de compras si no existe y si no esta logueado
    una vez se loguee se lo asocia a el usuario"""
    user = request.user if request.user.is_authenticated else None
    cart_id = request.session.get('cart_id')
    cart = Cart.objects.filter(cart_id=cart_id).first() #Retorna una lista

    if cart is None:
        cart = Cart.objects.create(user=user)

    if user and cart.user is None:
        cart.user = user
        cart.save()


    request.session['cart_id'] = cart.cart_id

    return cart


    '''CREAR UNA SESSION'''
    #request.session['cart_id'] = '123'  #DIC

    '''OBTENER EL VALOR DE UNA SESSION'''
    #valor = request.session.get('cart_id')
    #print(valor)

    ''''ELIMINAR UNA SESSON'''
    #request.session['cart_id'] = None
    #print(valor)
