from django.http import HttpResponse
from django.template import loader
import math


def index(request):
    template = loader.get_template('dot_and_circle/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def check(request):
    if request.GET.get('xCircle') \
            and request.GET.get('yCircle') \
            and request.GET.get('xPoint') \
            and request.GET.get('yPoint') \
            and request.GET.get('radius'):
        x_circle = float(request.GET.get('xCircle'))
        y_circle = float(request.GET.get('yCircle'))
        x_point = float(request.GET.get('xPoint'))
        y_point = float(request.GET.get('yPoint'))
        radius = float(request.GET.get('radius'))
    else:
        return HttpResponse(status=400)
    return HttpResponse(
        is_the_dot_inside_the_circle(x_circle,
                                     y_circle,
                                     x_point,
                                     y_point,
                                     radius))


def is_the_dot_inside_the_circle(x_circle, y_circle, x_point, y_point, radius):
    delta_x = x_circle - x_point
    delta_y = y_circle - y_point
    distance = math.sqrt((delta_x * delta_x) + (delta_y * delta_y))
    return distance < radius