from django import template

register = template.Library()
 
@register.filter
def get_item(dictionary, key):
    """Template filter to get dictionary items by key"""
    return dictionary.get(key, []) 