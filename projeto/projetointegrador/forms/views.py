from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def forms(request):
    return render(request, 'home.html')
