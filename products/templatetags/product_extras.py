"""
Este es un filtro que se crea para darle formato a el precio simplemente es
creado a manera de ejemplo de filtros donde para poder definir la función como filtro
se le "decora" con el @register_filter() no sin antes importar template y instanciar
el objeto register con la clase Library()"""


from django import template

register = template.Library()

@register.filter()
def price_format(value):
    return '${0:.2f}'.format(value)
