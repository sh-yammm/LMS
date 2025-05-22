from django import template

register = template.Library()

@register.simple_tag
def convert_uppercase(text):

    return text.upper()

@register.simple_tag
def user_role_checking(request , roles):

    role = roles.split(',')

    if request.user.is_authenticated and request.user.role in roles :

        return True
    
    return False