from django.http import HttpResponse
from django.template import loader
import qrcode
import base64
from django.shortcuts import get_object_or_404, render
from io import BytesIO

def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render({}, request))

def forms(request):
    template = loader.get_template("formulario.html")
    return HttpResponse(template.render({}, request))

def cadastro(request):
    print(request.POST)
    texto_qrcode = request.POST.get("cpf") + 'id'
    img = qrcode.make(texto_qrcode)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    qr_img_bytes = base64.b64encode(buffered.getvalue()).decode("ascii")
    template = loader.get_template("formulario.html")
    return HttpResponse(template.render({"qrcode": qr_img_bytes}, request))