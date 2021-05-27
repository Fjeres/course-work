from django import template

from cars.models import CarModel, Cars

register = template.Library()


@register.simple_tag(name='get_list_model')
def get_model():
    return CarModel.objects.all()

