"""---------------------------
Este es un filtro que se crea para colocar plural en el texto de producto agregado a el
carrito de compras donde para poder definir la función como filtro
se le "decora" con el @register_filter() no sin antes importar template e instanciar
el objeto register con la clase Library()
---------------------------"""
from django import template

register = template.Library()

@register.filter()
def quantity_product_format(quantity=1):
    return '{} {}'.format(quantity, 'Productos' if quantity > 1 else 'Producto')

@register.filter()
def quantity_add_format(quantity=1):
    return '{} {}'.format(
        quantity_product_format(quantity),
        'agregados' if quantity > 1 else 'agregado'
    )
