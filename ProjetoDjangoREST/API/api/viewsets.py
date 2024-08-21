from rest_framework import viewsets
from API.api import serializers
from API import models

class JogosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.JogosSerializers
    queryset = models.Jogos.objects.all()