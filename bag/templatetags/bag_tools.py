from django import template

# Calculate the subtotal by multiplying the price and quantity.
register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity