#cUSTOM TEMPLATE FILTERS

#REGISTERING FILTERS WITH A LIBRARY
from django import template
register = template.Library()

#REGISTERING FILTERS WITH DECORATORS
@register.filter(name='cut')

#FUNCTION THAT IS CUSTOM FILTER TEMPLATE
#value= var of whatever context_dict, and any additional argument
def cut(value,arg):
    #dot string
    """
    This cuts out all values of "arg" from the string!"
    """
    #grab the value, .replace() what you are looking for "arg"
    #and what you want to replace it with, what is assumed a "string"
    return value.replace(arg, '')

#EXAMPLE IF YOU DONT WANT TO USE DECORATORS: pass in as a string what you want to call the filter and pass through the function itself
# register.filter('cut', cut)
