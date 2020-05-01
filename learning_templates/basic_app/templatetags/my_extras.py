# Here we are definning a Custome Template Filters

from django import template

register = template.Library()

def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

# Need to register the funtion to use as Template Filter
register.filter('cut', cut)
# argument 1: string name of the filter which we use in template Filter
# argument 2: the actual function name
