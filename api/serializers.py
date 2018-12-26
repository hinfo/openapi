from rest_framework import serializers
from .models import *


class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ["id", "nome", "canal", "valor", "obs"]
