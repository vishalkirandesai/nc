from django.http import HttpResponse
from django.template import loader


def index(request):
    return HttpResponse("Hello, world.")

def index(request):
    lies_inside = True
    template = loader.get_template('dot_and_circle/index.html')
    context = {
        'lies_inside': lies_inside,
    }
    return HttpResponse(template.render(context, request))
