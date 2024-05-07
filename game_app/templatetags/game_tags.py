from django import template

from game_app.models import Category

register = template.Library()

@register.simple_tag(name='get_categories')
def get_categories():
    return Category.objects.all()