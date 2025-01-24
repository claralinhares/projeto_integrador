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

def scanner_for_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":
        try:
            body = json.loads(request.body)
            qr_data = body.get("qr_data")

            # Verifica se o participante existe
            participant = Participant.objects.get(qr_code_data=qr_data, event=event)
            if participant.is_present:
                return JsonResponse({"status": "error", "message": "Presença já registrada!"})

            # Marca o participante como presente
            participant.is_present = True
            participant.save()
            return JsonResponse({"status": "success", "message": "Presença registrada com sucesso!"})

        except Participant.DoesNotExist:
            return JsonResponse({"status": "error", "message": "QR Code inválido ou participante não encontrado!"})

        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Dados inválidos enviados no corpo da solicitação!"})

    return render(request, "scanner.html", {"event": event})