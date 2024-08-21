from rest_framework import serializers
from API import models

class JogosSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Jogos
        fields = '__all__'