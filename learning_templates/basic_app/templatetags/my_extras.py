# Custom build template tag filters/formats
from django import template

register = template.Library()


@register.filter(name="cut")
def cut(value, arg):
    """ This cuts out all values of 'arg' from the string """
    return value.replace(arg, '')


# Could register with the decorator above or like this:
# register.filter('cut', cut)
