from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    #This cuts out all the values of arg from string!
    return value.replace(arg,'')
