from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render({}, request))

def forms(request):
    template = loader.get_template("formulario.html")
    return HttpResponse(template.render({}, request))