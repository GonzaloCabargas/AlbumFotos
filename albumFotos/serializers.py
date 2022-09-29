
# este archivo se encarga de convertir los datos a json o desde json
#tmbn funciones crud

from pyexpat import model
from .models import Foto
from rest_framework import serializers

class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foto
        fields = '__all__'
