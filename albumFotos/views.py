from django.shortcuts import render
from .models import Foto
from rest_framework import viewsets
from .serializers import FotoSerializer
# Create your views here.

class FotoViewset(viewsets.ModelViewSet):
    queryset = Foto.objects.all()
    serializer_class = FotoSerializer

    def get_queryset(self):
        fotos = Foto.objects.all()

        titulo = self.request.GET.get('titulo')
        if titulo:
            fotos = fotos.filter(titulo__contains=titulo)
        return fotos

def home(request):
    return render(request, 'home.html')

def album(request):
    fotos = Foto.objects.all()
    data = {
        'fotos':fotos
    }

    return render(request, 'album.html',data)