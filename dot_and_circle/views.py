from django.http import HttpResponse
from django.template import loader
import math

def index(request):
    template = loader.get_template('dot_and_circle/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def check(request):
    radius = float(request.GET.get('radius'))
    xCircle = float(request.GET.get('xCircle'))
    yCircle = float(request.GET.get('yCircle'))
    xPoint = float(request.GET.get('xPoint'))
    yPoint = float(request.GET.get('yPoint'))

    return HttpResponse(
        is_the_dot_inside_the_circle(xCircle,
                                     yCircle,
                                     xPoint,
                                     yPoint,
                                     radius))

def is_the_dot_inside_the_circle(xCircle, yCircle, xPoint, yPoint, radius):
    deltaX = xCircle - xPoint
    deltaY = yCircle - yPoint
    distance = math.sqrt((deltaX * deltaX) + (deltaY * deltaY))
    return distance < radius
