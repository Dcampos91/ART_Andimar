import json
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views import View
from .models import *
from encuesta.settings import DATABASES
from .services import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .serializers import *
from django.contrib import messages

def home(request):
    data = {
        'listado':get_postura()
    }
    return render(request, 'core/encuesta.html',data)


def status(request):
    data = {
        'resultado': get_chofer(request)
    }    
    return render(request, 'core/encuesta.html',data)


class PosturaTotalView(viewsets.ModelViewSet):
    queryset = TablaPostura.objects.all()
    serializer_class = PosturaTotalSerializer




