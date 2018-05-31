from django import template

register = template.Library()

@register.filter
def cutr(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(' ', arg)\

@register.filter
def toman(value):
    """Removes all values of arg from the given string"""
    return value+' تومان '