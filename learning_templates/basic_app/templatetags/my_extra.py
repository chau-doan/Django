from django import template

register = template.Library()

@register.filter(name='cut') # cut func either have or not doesn't effect
def cut(value, arg):
  """
  This cuts out all values of "arg" from the string!

  """
  return value.replace(arg,'')

# register.filter('cut', cut) can replace the @register.filter(name='func')