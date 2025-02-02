from django.http import HttpResponse
from django.template import loader
import qrcode
import base64
from django.shortcuts import get_object_or_404, redirect, render
from io import BytesIO
from .models import Event, Participant
from django.http import JsonResponse
import json
from django.contrib import messages


def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render({}, request))

def forms(request):
    template = loader.get_template("formulario.html")
    eventos = Event.objects.all()
    return HttpResponse(template.render({'eventos': eventos}, request))

def cadastro(request):
    texto_qrcode = request.POST.get("cpf") + 'id'
    img = qrcode.make(texto_qrcode)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    qr_img_bytes = base64.b64encode(buffered.getvalue()).decode("ascii")
    template = loader.get_template("formulario.html")
   
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        cpf = request.POST.get("cpf")
        event = request.POST.get("event")

        try:
            Participant.objects.create(nome=nome, email=email, cpf=cpf, qr_code_data=qr_img_bytes, event=Event.objects.get(id=event))
            messages.success(request, "Participante cadastrado com sucesso!")
        except Exception as e:
            messages.error(request, f"Erro ao cadastrar participante: {e}")

    return HttpResponse(template.render({"qrcode": qr_img_bytes}, request))



def create_event(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        date = request.POST.get("date")
        location = request.POST.get("location")

        try:
            Event.objects.create(name=name, description=description, date=date, location=location)
            messages.success(request, "Evento cadastrado com sucesso!")
        except Exception as e:
            messages.error(request, f"Erro ao cadastrar evento: {e}")

        return redirect ("create_event")

    return render(request, "create_event.html")

def list_events(request):
    eventos = Event.objects.all()  # Ou outra lógica para filtrar eventos
    return render(request, 'list_events.html', {'eventos': eventos})

def scanner_for_event(request, qr_code_data):
    try:
        # Caso o QR Code esteja vinculado a um modelo
        event = get_object_or_404(Event, qr_code_field=qr_code_data)  # Altere "qr_code_field" para o campo correto
        return render(request, 'scanner_result.html', {'event': event})
    except Exception as e:
        # Caso algo dê errado
        return render(request, 'scanner_error.html', {'error': str(e)})